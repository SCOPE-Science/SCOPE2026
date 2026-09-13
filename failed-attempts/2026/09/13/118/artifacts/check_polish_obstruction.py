"""Bounded recovery test: Polish-subspace obstruction for rank-one mixing.

Formalizes the Baire-category chain blocking direct turbulence inheritance:
dense(R cap M) + meager(R cap M) contradicts Polish=>G-delta=>comeager.

Flags encode established ergodic-theory facts (Halmos conjugacy lemma,
Halmos-Rohlin meagerness of mixing, Ornstein rank-one mixing existence,
Kechris 3.11 Polish=>G_delta, Baire):
  No computation proves the ergodic facts; the script checks the logical chain.
"""
FLAGS = {
    "MPT_polish": True,
    "mixing_meager_in_MPT": True,  # Halmos-Rohlin
    "ornstein_rankone_mixing_exists": True,  # Ornstein 1970s
    "aperiodic_orbit_dense": True,  # Halmos conjugacy lemma
    "conjugacy_preserves_rankone_mixing": True,
    "polish_subspace_implies_Gdelta": True,  # Alexandrov/Kechris 3.11
    "dense_Gdelta_in_polish_is_comeager": True,  # Baire
}

def main():
    dense = FLAGS["ornstein_rankone_mixing_exists"] and FLAGS["aperiodic_orbit_dense"] \
        and FLAGS["conjugacy_preserves_rankone_mixing"]
    meager = FLAGS["mixing_meager_in_MPT"]  # subset of mixing is meager
    polish_implies_Gdelta = FLAGS["polish_subspace_implies_Gdelta"]
    Gdelta_dense_implies_comeager = FLAGS["dense_Gdelta_in_polish_is_comeager"]
    print(f"dense(R cap M in MPT): {dense}")
    print(f"meager(R cap M in MPT): {meager}")
    # If Polish in subspace topology => G-delta in MPT => dense G-delta => comeager,
    # contradicting meager (in a non-empty perfect Polish space meager != comeager).
    if dense and meager and polish_implies_Gdelta and Gdelta_dense_implies_comeager:
        print("RESULT: NOT_POLISH — 'Polish subspace (weak topology)' premise is false as stated.")
        print("Consequence: Hjorth turbulence cannot be applied directly; needs new topology + re-verification.")
        # Turbulent-piece check: no dense-Gdelta-in-MPT piece can sit inside a meager set.
        print("RESULT: no ambient-G-delta comeager-in-RcapM turbulent piece without new topology.")
    else:
        print("RESULT: chain not triggered")

if __name__ == "__main__":
    main()
