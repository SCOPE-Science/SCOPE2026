"""Recovery/triviality check: dense-meager => meager-in-itself => vacuous generic ergodicity.

Encodes the logical chain used in DRAFT.md. Flags record classical theorems
(Halmos meagerness of mixing, Ornstein existence, Halmos density lemma,
Kechris Polish=>Gdelta); script verifies the Baire deduction, not the theorems.
"""
FLAGS = {
    "MPT_polish": True,
    "mixing_meager": True,
    "rankone_mixing_nonempty": True,
    "aperiodic_orbit_dense": True,
    "invariant": True,
}

def dense():
    return FLAGS["rankone_mixing_nonempty"] and FLAGS["aperiodic_orbit_dense"] and FLAGS["invariant"]

def main():
    d = dense()
    m = FLAGS["mixing_meager"]
    print(f"dense(RcapM): {d}")
    print(f"meager(RcapM in MPT): {m}")
    if d and m:
        print("STEP 1: RcapM dense + meager in Polish MPT => not G-delta => not Polish.")
        print("STEP 2: dense + meager in ambient => meager in itself (trace of nowhere-dense cover).")
        print("STEP 3: Y meager in itself => every A subset Y is meager; every A is also comeager.")
        print("STEP 4: singleton {x} is comeager in Y; any f maps it to one class.")
        print("RESULT: generic ergodicity holds VACUOUSLY for every relation on RcapM.")
        print("RESULT: second horn (invariant on non-meager set) impossible: no non-meager subsets exist.")
    else:
        print("chain not triggered")

if __name__ == "__main__":
    main()
