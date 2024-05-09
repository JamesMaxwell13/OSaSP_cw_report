#!/usr/bin/python3
import subprocess
import platform
import os
import sysconfig

# DOCKER_IMAGE = "ghcr.io/fcsan-bsuir/bsuir_tex:main"
DOCKER_IMAGE = "ajiob/docker-xelatex-fonts:1.2.1"

def main():
    system = platform.system()

    compile_cmd = "make -j4 -C 'src' all"

    clean_cmd = "make -C 'src' clean"
    
    docker_platform_flag = '--platform linux/amd64' if sysconfig.get_platform().split("-")[-1].lower() == 'arm64' else ''
    run_docker_cmd = f'docker run {docker_platform_flag} -i --rm -v "{os.getcwd()}:/test" -w /test {DOCKER_IMAGE} sh -c'

    cmd = " ".join([run_docker_cmd, "\"", compile_cmd, "&&" , clean_cmd, "\""])
    # cmd = " ".join([run_docker_cmd, "\"", compile_cmd])
    print(f"Running command:\n{cmd}")

    subprocess.run(cmd, shell=True)

if __name__=="__main__":
    main()