from typing import Any, Optional, Callable
import os
import time
import sys


SYS_VERSION: dict[str, str] = {
    "major": "1",
    "minor": "9",
    "micro": "0",
    "release": "beta"
}


class Main:
    def __init__(self, *args) -> None:
        self.dir: str = "c:/Users/janak/Documents/"
        self.atomic: dict[str, Any] = {}
        prefix: str = ""
        while True:
            rs: list[str] = input(f"{self.dir} -> " + prefix).strip().split(";")

            for r in rs:
                r = prefix + r
                if r.startswith("cd "):
                    self.parseCd(r)
                elif r.startswith("-cup "):
                    if r == "-cup ":
                        continue
                    self.parseCupm(r)
                elif r == "pscd":
                    os.system(f"cd {self.dir}")
                elif "=" in r:
                    parts: list[str] = r.split("=")
                    key: str = parts[0].strip()
                    value: str = parts[1].strip()
                    self.atomic.update({parts[0]: parts[1]})
                else:
                    os.system(r)

    def parseCd(self, r: str) -> None:
        f: str = r[3:].strip()
        if f.lower().startswith("c:/"):
            self.dir = "c:/" + f[3:]
        elif f == "..":
            self.dir = "/".join(self.dir[:-1].split("/")[:-1]) + "/"
        else:
            self.dir += f + "/"
        if self.dir == "/":
            self.dir = "c:/"

    def parseCupm(self, r: str) -> None:
        f: str = r[5:].strip()
        parts: list[str] = f.split(" ")
        sector: str = parts[0]
        action: str = parts[1]

        args: list[Any] = self.parseArgs(parts[2:]) if len(parts) != 2 else []

        self.CupmFuncs(sector, action, args)
    
    def CupmFuncs(self, sector: str, action: str, args: list[Any]):
        match sector:
            case "@basic":
                match action:
                    case "-print":
                        print("".join([str(arg) for arg in args]))
                    case "-ping":
                        start: float = time.perf_counter()
                        for _ in range(1_000_000):
                            ...
                        stop: float = time.perf_counter()
                        print(f"Pong! {stop - start}ms")
                    case "-exit":
                        exit(args[0])
            case "@external.python":
                match action:
                    case "-run-external":
                        os.system(f"python{args[1]} {args[0]}")
                    case "-run-internal":
                        exec(args[0])
                    case "-console":
                        print("(i) cupm- entering single-line python console")
                        os.system(f"python{args[0]}")
                    case "-version":
                        print(sys.version)
                        print("(i) cupm- upgrade your python at https://python.org/downloads")
                    case "-version-info":
                        print(sys.version_info)
                    case "-path":
                        print("\n\n    ".join(sys.path))
            case "@external.cmd":
                match action:
                    case "-echo":
                        os.system(f"echo {args[0]}")
                    case "-configure-ip":
                        print("(i) cupm- this may contain sensitive information that will not be saved after\n          the program has ended")
                        os.system("ipconfig")
                    case "-ping":
                        for i in range(args[1]):
                            print("\n\n\n\n(i) cupm- iteration " + str(i + 1))
                            os.system(f"ping {args[2]} {args[0]}")
                    case "-read-file":
                        os.system(f"cat {self.dir + args[0]}")
                    case "-cd":
                        os.system(f"cd {args[0]}")
                    case "-write-file":
                        os.system(f"echo {args[1]} > {self.dir + args[0]}")
                    case "-cmd":
                        os.system(args[0])
                    case "-help":
                        os.system(f"help {args[0]}")

            case "@external.pip":
                match action:
                    case "-run":
                        os.system(f"pip {args[0]}")
                    case "-install":
                        os.system(f"pip install {args[0]}")
                    case "-upgrade":
                        os.system("python.exe -m pip install --upgrade pip")
                    case "-help":
                        os.system(f"pip help {args[0]}")
                    case "-packages":
                        os.system("pip list")
                    case "-package":
                        os.system(f"pip show {args[0]}")
                    case "-configure-pip":
                        os.system(f"pip config {args[0]}")

            case "@atomic":
                match action:
                    case "-set":
                        if len(args) == 3:
                            if args[2] == "String":
                                self.atomic.update({args[0]: "\"" + args[1] + "\""})
                        else:
                            self.atomic.update({args[0]: args[1]})
            case "@basic.math":
                match action:
                    case "+":
                        self.atomic.update({args[0]: args[1] + args[2]})
                    case "-":
                        self.atomic.update({args[0]: args[1] - args[2]})
                    case "*":
                        self.atomic.update({args[0]: args[1] * args[2]})
                    case "/":
                        self.atomic.update({args[0]: args[1] / args[2]})
                    case "%":
                        self.atomic.update({args[0]: args[1] % args[2]})
                    case "++":
                        self.atomic.update({args[0]: sum(*args[1:])})
            case "@cupm":
                match action:
                    case "-version":
                        print("RELE.:" + SYS_VERSION["release"])
                        print("MAJOR:" + SYS_VERSION["major"])
                        print("MINOR:" + SYS_VERSION["minor"])
                        print("MICRO:" + SYS_VERSION["micro"])

    def parseArgs(self, parts: list[str]) -> list[Any]:
        args: list[Any] = []
        i: int = 0
        while True:
            if parts[i].startswith("$"):
                key: str = parts[i].strip("$").strip()
                parts[i] = str(self.atomic.get(key))
            if parts[i].startswith("\""):
                i2: int = i
                try:
                    while True:
                        if parts[i2].endswith("\""):
                            args.append(" ".join(parts[i:i2 + 1]).strip("\""))
                            break
                        i2 += 1
                except IndexError:
                    raise SyntaxError("' \" ' was not closed")
                i = i2
                del i2
            elif parts[i].replace("_", "").isnumeric():
                args.append(int(parts[i].strip()))
            elif parts[i].strip() == "":
                continue
            if i == len(parts) - 1:
                break
            i += 1
        return args


if __name__ == "__main__":
    _: Main = Main("__main__")
