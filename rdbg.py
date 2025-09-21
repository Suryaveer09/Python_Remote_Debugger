# rdbg.py
import argparse, runpy, sys, debugpy

def main():
    p = argparse.ArgumentParser("Run a script under a remote debugger")
    p.add_argument("--host", default="127.0.0.1")  # safer default
    p.add_argument("--port", type=int, default=5678)
    p.add_argument("--wait", action="store_true")
    p.add_argument("script")
    p.add_argument("script_args", nargs=argparse.REMAINDER)
    a = p.parse_args()

    debugpy.listen((a.host, a.port))
    print(f"[rdbg] listening on {a.host}:{a.port}")
    if a.wait:
        print("[rdbg] waiting for debugger to attach...")
        debugpy.wait_for_client()

    sys.argv = [a.script] + a.script_args
    runpy.run_path(a.script, run_name="__main__")

if __name__ == "__main__":
    main()
