"""Degree check for lane-865 stem-70 Ctau transfer (TARGET disproof).

Encodes the bigraded degrees of the cofiber-of-tau LES boundary and of
Betti realization, and checks the literal target equality for impossibility.

Triangle: S^{0,-1} --tau--> S --c--> Ctau --d--> S^{1,-1} = Sigma^{1,-1} S.
  boundary d_*: pi_{s,w}(Ctau) -> pi_{s-1,w+1}(S_mot)
  Betti Re_*: pi_{s-1,w+1}(S_mot) -> pi_{s-1}(S_cl)
Hence composite pi_{70,w}(Ctau) -> pi_{69}(S_cl) for every weight w.
Literal target demands equality with 2.x in pi_{70}(S_cl). Different groups.

Run: python3 output/artifacts/verify.py  -> prints VERIFY_OK on success.
Stdlib only.
"""
SOURCE_STEM = 70
TARGET_STEM_CLAIMED = 70

def les_boundary_degree(s, w):
    """Degree of d_*: [S^{s,w}, Ctau] -> [S^{s,w}, S^{1,-1}]."""
    # [S^{s,w}, S^{1,-1}] = pi_{s-1, w+1}
    return (s - 1, w + 1)

def betti_degree(s, w):
    """Re_*: pi_{s,w}(mot S) -> pi_s(cl S)."""
    return s

def composite_stem(s, w):
    bs, bw = les_boundary_degree(s, w)
    return betti_degree(bs, bw)

def main():
    # 1. Check all weights land in 69, never 70.
    for w in range(-5, 15):
        assert composite_stem(SOURCE_STEM, w) == 69, (SOURCE_STEM, w)
        assert composite_stem(SOURCE_STEM, w) != TARGET_STEM_CLAIMED
    # 2. Weight-independence: classical stem does not see w.
    stems = {composite_stem(SOURCE_STEM, w) for w in range(-10, 30)}
    assert stems == {69}, stems
    # 3. Only source stem 71 could land in classical 70.
    assert composite_stem(71, 36) == 70
    # 4. Groups pi_69 vs pi_70 are distinct; cross-group equality is ill-typed.
    assert 69 != 70
    print("VERIFY_OK: source stem 70 -> composite stem 69 for all weights; "
          "equality in pi_70 impossible as stated.")

if __name__ == "__main__":
    main()
