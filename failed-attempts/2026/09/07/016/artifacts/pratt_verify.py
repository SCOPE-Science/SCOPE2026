#!/usr/bin/env python3
"""Standalone Pratt verifier: checks certs/*.json with only stdlib modular arithmetic.
Usage: python3 pratt_verify.py certs_dir
Checks for each cert file (except _summary.json):
  g^(q-1) == 1 mod q, g^((q-1)/r) != 1 for each distinct prime factor r,
  product r^e == q-1, recursive certs valid. Reports PASS/FAIL per file.
"""
import json, sys, os, glob

def verify(cert):
    q = cert["q"]
    if q == 2:
        if cert.get("factors"):
            raise ValueError("q=2 must have empty factors")
        return True
    g = cert["g"]
    factors = cert["factors"]
    prod = 1
    for f in factors:
        prod *= f["prime"]**f["exp"]
    if prod != q-1:
        raise ValueError(f"q={q}: product {prod} != q-1")
    if not (1 < g < q):
        raise ValueError(f"q={q}: witness g={g} out of range")
    if pow(g, q-1, q) != 1:
        raise ValueError(f"q={q}: g^(q-1) != 1")
    for f in factors:
        r = f["prime"]
        if pow(g, (q-1)//r, q) == 1:
            raise ValueError(f"q={q}: g^((q-1)/{r}) == 1")
        verify(f["cert"])
    return True

def main():
    d = sys.argv[1] if len(sys.argv)>1 else "output/artifacts/certs"
    files = sorted(glob.glob(os.path.join(d, "*.json")))
    files = [f for f in files if not f.endswith("_summary.json")]
    nfail = 0
    for fp in files:
        with open(fp) as f:
            cert = json.load(f)
        try:
            verify(cert)
            print(f"PASS {os.path.basename(fp)} q={cert['q']} g={cert['g']}")
        except Exception as e:
            nfail += 1
            print(f"FAIL {os.path.basename(fp)}: {e}")
    print(f"verified {len(files)} certs, failures={nfail}")
    sys.exit(1 if nfail else 0)

if __name__ == "__main__":
    main()
