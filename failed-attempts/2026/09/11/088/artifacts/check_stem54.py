"""Replayable census: stem-53/54 rows in IW-X algebraic-Novikov CSVs.

Shows (stdlib only) that the machine-readable sources record algebraic-Novikov
differentials converging to AN E2 -- not Adams-Novikov d3 values -- so no
beta-family ANSS d3 ledger at stem 54 is contained in them.

Sources: Zenodo record 6987227 (Isaksen-Wang-Xu):
  output/artifacts/algNovikov-machine.csv  (algNov E2 page + algNov differentials)
  output/artifacts/algNovikov-Einfty.csv   (algNov E-infinity = AN E2, Adams names)
Usage: python3 output/artifacts/check_stem54.py
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MACHINE = os.path.join(HERE, "algNovikov-machine.csv")
EINF = os.path.join(HERE, "algNovikov-Einfty.csv")


def main():
    with open(MACHINE) as f:
        r = csv.DictReader(f)
        print("machine header:", r.fieldnames)
        rows = list(r)
    assert "drinfo" in r.fieldnames and "drvalue" in r.fieldnames
    # ANSS d3 would need its own column; none exists.
    assert not any("anss" in (c or "").lower() or "novikov-d3" in (c or "").lower()
                   for c in r.fieldnames), "unexpected ANSS d3 column"
    s54 = [x for x in rows if x["stem"].strip() == "54"]
    s53 = [x for x in rows if x["stem"].strip() == "53"]
    print("machine rows: stem54 =", len(s54), "| stem53 =", len(s53))
    print("--- stem54 rows with algNov differentials ---")
    for x in s54:
        if x["drinfo"].strip() or x["drvalue"].strip():
            print(x["name"], "| filt", x["Adams filtration"],
                  "| algNov d" + x["drinfo"].strip(), "->", x["drvalue"])
    print("--- stem53 machine rows (candidate ANSS-d3 targets would live here) ---")
    for x in s53:
        print(x["name"], "| filt", x["Adams filtration"],
              "| algNov dr:", (x["drinfo"].strip() or "-"), "->", (x["drvalue"] or "-"))
    with open(EINF) as f:
        r2 = csv.DictReader(f)
        einrows = [x for x in r2 if x["stem"].strip() in ("53", "54")]
    print("--- algNov E-infinity (= AN E2) stems 53/54 ---")
    for x in einrows:
        print(x["name"], "| stem", x["stem"], "| filt", x["Adams filtration"])
    print("CENSUS_OK: no ANSS-d3 ledger present in these files")


if __name__ == "__main__":
    main()
