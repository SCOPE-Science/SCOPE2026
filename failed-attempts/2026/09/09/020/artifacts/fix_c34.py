"""Fix C3x4.json: CD(G)={G} for abelian G (was mislabeled as full lattice).
Keeps rank/Sperner subgroup-lattice data under separate keys."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, "results", "C3x4.json")
r = json.load(open(p))
N = r["n"]
full = sorted(range(N))
r["sublattice_width"] = r.pop("width")
r["sublattice_width_rank"] = r.pop("width_rank")
r["sublattice_width_witness"] = r.pop("width_witness")
# Correct CD data by the abelian lemma (m(H)=|H|*|G| max uniquely at H=G)
r["m"] = N * N
r["cd_size"] = 1
r["width"] = 1
r["is_chain"] = True
r["is_quasi_antichain"] = True
r["cd_subgroup"] = full
r["cd_members"] = [full]
r["cd_orders"] = [N]
r["cd_covers"] = []
r["width_witness"] = [full]
r["cd_note"] = "CD(G)={G} by abelian lemma; width-130 datum is the SUBGROUP-lattice width (Sperner)"
json.dump(r, open(p, "w"))
print("patched C3x4: |CD|=1, CD={G}, sublattice_width=130")
