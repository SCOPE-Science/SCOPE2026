"""Run full census: rectangles R x C for R in 2..6, C in 6..10, both directions.
Writes counts_<RxC-D>.json + census_summary.json. Prints progress."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tm import enumerate_case
from fractions import Fraction

SURVEY = {"0.40": Fraction(2, 5), "0.45": Fraction(9, 20), "0.50": Fraction(1, 2),
          "0.55": Fraction(11, 20), "0.60": Fraction(3, 5),
          "0.44": Fraction(11, 25), "0.56": Fraction(14, 25)}

def probs_of(res):
    m = res["m"]
    out = {}
    for name, p in SURVEY.items():
        q = 1 - p
        tot = Fraction(0)
        for k, c in enumerate(res["cross_counts"]):
            if c:
                tot += c * p ** k * q ** (m - k)
        out[name] = [tot.numerator, tot.denominator, float(tot)]
    return out

def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    cases = [(R, C) for R in (2, 3, 4, 5, 6) for C in (6, 7, 8, 9, 10)]
    filt = os.environ.get("CASES")
    if filt:
        cases = [tuple(map(int, s.split("x"))) for s in filt.split(",")]
    summary = []
    t0 = time.time()
    for (R, C) in cases:
        for d in ("H", "V"):
            tag = f"{R}x{C}-{d}"
            t1 = time.time()
            print(f"[{time.time()-t0:7.1f}s] case {tag} ...", flush=True)
            res = enumerate_case(R, C, d)
            res["probs"] = probs_of(res)
            fn = os.path.join(outdir, f"counts_{tag}.json")
            tmp = fn + ".tmp"
            with open(tmp, "w") as f:
                json.dump(res, f)
            os.replace(tmp, fn)
            row = {"case": tag, "m": res["m"],
                   "P": {k: v[2] for k, v in res["probs"].items()}}
            summary.append(row)
            print(f"[{time.time()-t0:7.1f}s]   done {tag} m={res['m']} "
                  f"P44={row['P']['0.44']:.6f} P56={row['P']['0.56']:.6f} "
                  f"P50={row['P']['0.50']:.6f} ({time.time()-t1:.1f}s)", flush=True)
    with open(os.path.join(outdir, "census_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print("ALL DONE", flush=True)

if __name__ == "__main__":
    main()
