import subprocess

def call_command(command_to_call):
    call = subprocess.check_call(command_to_call, shell=True)
    output = subprocess.check_output(command_to_call, shell=True)
    return call, output[:-1]

res = call_command("echo '6.5 / 2.7' | bc")
print(res[0], res[1])
print(type(res[0]), type(res[1]))
