"""Independent verifier: re-runs the ledger from integer inputs and
byte-compares ledger.json / replay.log. Prints VERIFY_OK or VERIFY_FAIL."""
import json
import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))

p = subprocess.run([sys.executable, os.path.join(HERE, "srg_ledger.py")],
                   cwd="/tmp", capture_output=True, text=True)
# NOTE: srg_ledger.py writes into CWD, so rerun into a temp dir and compare.
import tempfile
with tempfile.TemporaryDirectory() as td:
    p2 = subprocess.run([sys.executable, os.path.join(HERE, "srg_ledger.py")],
                        cwd=td, capture_output=True, text=True)
    if p2.returncode != 0:
        print("VERIFY_FAIL: rerun error")
        print(p2.stderr[-2000:])
        sys.exit(1)
    for name in ("ledger.json", "replay.log"):
        a = open(os.path.join(HERE, "..", "..", name)
                 if False else os.path.join(td, name), "rb").read()
        b = open(os.path.join(HERE, name), "rb").read() \
            if os.path.exists(os.path.join(HERE, name)) else None
        # artifacts live in the same dir as this script
        ref = os.path.join(HERE, name)
        # ledger.json/replay.log were written to CWD at generation time;
        # canonical copies are stored alongside this script? No:
        # they are in output/artifacts/. Handle both.
        cands = [os.path.join(HERE, name),
                 os.path.join(os.path.dirname(HERE), name)]
        found = None
        for c in cands:
            if os.path.exists(c):
                found = open(c, "rb").read()
                break
        new = open(os.path.join(td, name), "rb").read()
        if found is None:
            print("VERIFY_FAIL: missing reference %s" % name)
            sys.exit(1)
        if new != found:
            print("VERIFY_FAIL: %s differs" % name)
            sys.exit(1)
print("VERIFY_OK")
