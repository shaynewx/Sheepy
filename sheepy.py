#!/usr/bin/env python3
import sys
import re

def match_shebang(line):  
    # check shebang
    if line.startswith("#!"):
        print("#!/usr/bin/python3 -u")

def match_emptyline(line):
    # check whether need to print empty line
    if line =='' or line =='do' or line =='done':
        print("")

def import_glob(shell_command):
    # check whether need to import glob
    flag = 0
    for line in shell_command:
        if re.search(r'(.*)[\*\?](.*)', line) or re.search(r'(.*)\[(.*)\](.*)', line):
            flag += 1
    if flag != 0:
        print("import glob")

def import_sys(shell_command):
    # check whether need to import sys
    flag = 0
    for line in shell_command:
        if re.search(r'(.*)exit(.*)', line) or re.search(r'(.*)\$(\d+)', line):
            flag += 1
    if flag != 0:
        print("import sys")

def import_os(shell_command):
    # check whether need to import os
    flag = 0
    for line in shell_command:
        if re.search(r'(.*)cd(.*)', line) :
            flag += 1
    if flag != 0:
        print("import os")

def import_subprocess(shell_command):
    # check whether need to import subprocess (pwd ls id date touch...)
    flag = 0
    for line in shell_command:
        commands_to_match = ['pwd', 'ls', 'id', 'date', 'touch', 'mkdir', 'chmod']
        if any(re.search(rf'(\s*){command}(.*)', line) for command in commands_to_match):
            flag += 1
    if flag != 0:
        print("import subprocess")

def match_comment(line):
    # check comments : if line contains any comments then print these comments and then delete
    result = re.search(r'(\s*)#(.*)', line)
    if result:
        if line.startswith("#!"):
            pass
        else:
            print(f"#{result.group(2)}")
            new_line = re.sub(r'#(.*)','',line).strip()
            if new_line !='':
                return new_line
    else:
        return line

def match_variable(line):
    # check variable
    result = re.search(r"(^[a-zA-Z]+.*)=(.*)", line)
    if result:
        name = result.group(1)
        variable = result.group(2)
        result2 = re.search(r'\$(.*)', variable)
        if result2:
            result3 = re.search(r'^(\d+)', result2.group(1))
            if result3:
                print(f"{name} = \"sys.argv[{result3.group(1)}]\"")
            else:
                variable = re.sub(r'\$(\w+)', r'{\1}', variable)
                variable =  "f" + variable
                result_line = f"{name} = \"{variable}\""
                print(result_line)
        else:
            print(f"{name} = \'{variable}\'")
    
def match_for(line):
    # check for loop
    result = re.search(r"(\s*)for(.*)in\s(.*)", line)
    if result:
        before_for = result.group(1)
        after_for = result.group(2).strip()
        after_in = result.group(3).strip()
        result2 = re.search(r'\*\.(\w+)', after_in)
        if result2:
            after_in = f'sorted(glob.glob("*.{result2.group(1)}"))'
        print(f"{before_for}for {after_for} in {after_in.split()}:")

def match_echo(line):
    # check echo
    result = re.search(r"(\s*)echo(.*)", line)
    if result:
        before_echo = result.group(1)
        after_echo = re.sub(r'\s+', ' ', (result.group(2)).strip())
        # check whether there is “echo *”
        if after_echo == "*":
            print("print(\" \".join(sorted(glob.glob(\"*\"))))")
        # if there is no "$" then print else modify the command
        else:
            # check whether there is “$num”
            result2 = re.search(r'(.*)\$(\d+)', after_echo)
            if result2:
                result2.group(2)
                print(f"{before_echo}print(f\"{result2.group(1)}{{sys.argv[{result2.group(2)}]}}\")")
            elif re.search(r'\$(\w+)', after_echo):
                after_echo = re.sub(r'(\$(\w+))(?!\$)', r'{\2}', after_echo)
                print(f'{before_echo}print(f\"{after_echo}\")')
            else:
                print(f"{before_echo}print(\"{after_echo}\")")       

def match_cd(line):
    # check cd
    result = re.search(r"(\s*)cd(.*)", line)
    if result:
        before_cd = result.group(1)
        after_cd = result.group(2).strip()
        print(f"{before_cd}os.chdir('{after_cd}')")


def match_subprocess(line):
    # check subprocess command
    result_pwd = re.search(r"(\s*)pwd(.*)", line)
    if result_pwd:
        before_pwd = result_pwd.group(1)
        after_pwd = result_pwd.group(2).strip()
        print(f"{before_pwd}subprocess.run(['pwd'])")

    result_id = re.search(r"(\s*)id(.*)", line)
    if result_id:
        before_id = result_id.group(1)
        after_id = result_id.group(2).strip()
        print(f"{before_id}subprocess.run(['id'])")

    result_date = re.search(r"(\s*)date(.*)", line)
    if result_date:
        before_date = result_date.group(1)
        after_date = result_date.group(2).strip()
        print(f"{before_date}subprocess.run(['date'])")

    result_ls = re.search(r"(\s*)ls(.*)", line)
    if result_ls:
        before_ls = result_ls.group(1)
        after_ls = result_ls.group(2).strip()
        if after_ls != None:
            list = (result_ls.group(0).split())
            print(f"{before_ls}subprocess.run({list})")

    result_touch = re.search(r"(\s*)touch(.*)", line)
    if result_touch:
        before_touch = result_touch.group(1)
        after_touch = result_touch.group(2).strip()
        if after_touch != None:
            list = (result_touch.group(0).split())
            print(f"{before_touch}subprocess.run({list})")
    
    result_mkdir = re.search(r"(\s*)mkdir(.*)", line)
    if result_mkdir:
        pass

    result_chmod = re.search(r"(\s*)chmod(.*)", line)
    if result_chmod:
        pass

def match_read(line):
    # check read
    result = re.search(r"(\s*)read(.*)", line)
    if result:
        before_read = result.group(1)
        after_read = result.group(2).strip()
        print(f"{before_read}{after_read} = input()")

def match_exit(line):
    # check exit
    result = re.search(r"(\s*)exit(.*)", line)
    if result:
        before_exit = result.group(1)
        after_exit = result.group(2).strip()
        if after_exit == "":
            print("sys.exit()")
        else:
            print(f"{before_exit}sys.exit({after_exit})")

if __name__ == '__main__':
    with open (sys.argv[1]) as file:
        lines = file.readlines()
    shell_command = [line.rstrip() for line in lines]

    # check shebang
    for line in shell_command:
        match_shebang(line)

    # check import
    import_glob(shell_command)
    import_sys(shell_command)
    import_os(shell_command)
    import_subprocess(shell_command)

    for line in shell_command:
        match_emptyline(line) # check empty line
        line = match_comment(line) # check comments
        if line != None:
            match_for(line) # check for loop
            match_variable(line) # check for variable
            match_echo(line) # check echo
            match_read(line) # check read
            match_exit(line) # check exit
            match_cd(line) # check cd
            match_subprocess(line) # check subprocess