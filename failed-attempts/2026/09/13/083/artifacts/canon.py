"""Canonical frozen dataset: veering triangulation + flipper corner data + track.

Regenerates deterministically: tries flipper bundles until the triangulation isosig
matches the frozen artifact V (gLLMQaedfdffjxaxjkn_aBbB); then dumps T3 peripheral
corner tables (M/L) to disk. All downstream scripts MUST load these frozen files and
must assert the live triangulation isosig matches, else abort.
"""
import pickle, sys
import snappy, flipper
from flipper.kernel.triangulation3 import MERIDIANS, LONGITUDES

WDIR = "output/artifacts"
FROZEN_ISOSIG = snappy.Manifold(f"{WDIR}/V_flipper_veering.tri").triangulation_isosig()
print("frozen isosig:", FROZEN_ISOSIG, flush=True)

def load_frozen():
    d = pickle.load(open(f"{WDIR}/corner_data.pkl", "rb"))
    assert d["isosig"] == FROZEN_ISOSIG, (d["isosig"], FROZEN_ISOSIG)
    return d

if __name__ == "__main__":
    # build corner_data.pkl from a live bundle matching frozen isosig (retry loop)
    import random
    for attempt in range(30):
        M = snappy.Manifold('10_145')
        mono = flipper.monodromy_from_bundle(M)
        B = mono.bundle(veering=True)
        V = snappy.Manifold(B.snappy_string())
        iso = V.triangulation_isosig()
        print(f"attempt {attempt}: {iso}", flush=True)
        if iso == FROZEN_ISOSIG:
            T3 = B.triangulation3
            corners = {}
            for P, name in [(MERIDIANS, "M"), (LONGITUDES, "L")]:
                tab = {}
                for t in T3.tetrahedra:
                    for s_ in range(4):
                        for o in range(4):
                            tab[(t.label, s_, o)] = t.peripheral_curves[P][s_][o]
                corners[name] = tab
            # tet label -> index correspondence: T3 tetrahedra labels vs SnapPy tet indices:
            # verify label set == range(NT)
            print("tet labels:", sorted(t.label for t in T3.tetrahedra), flush=True)
            print("fibre:", B.fibre_slopes(), "degen:", B.degeneracy_slopes(), flush=True)
            print("int(m,l):", T3.intersection_number(MERIDIANS, LONGITUDES), flush=True)
            pickle.dump({"isosig": iso, "corners": corners,
                         "fibre": B.fibre_slopes(), "degen": B.degeneracy_slopes()},
                        open(f"{WDIR}/corner_data.pkl", "wb"))
            print("FROZEN corner_data.pkl written", flush=True)
            break
    else:
        print("FAILED to match frozen isosig in 30 attempts", flush=True)
        sys.exit(1)
