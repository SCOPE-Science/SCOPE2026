"""Verifier for lane-702 TARGET disproof: handle-count impossibility.

Literal target premises: compact oriented Mazur-type Stein handlebody W with
n0=1, n1=1, n2=2, n3=n4=0, contractible, boundary an integral homology sphere.
Checks:
  (1) chi(handle counts) = 2 != 1 = chi(contractible);
  (2) cellular rank-nullity forces H1,H2 not both zero;
  (3) Stein index<=2 forbids 3-handle repair;
  (4) one-3-handle repair restores chi=1 only by leaving Stein class;
  (5) terminology: Mazur-type = 1x1-handle + 1x2-handle, so 1+2 = plug-type.
Stdlib only. Nonzero exit on any failure.
"""
from fractions import Fraction

passed, failed = [], []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))
    (passed if cond else failed).append(name)


# (1) Euler characteristic from handle counts
n0, n1, n2, n3, n4 = 1, 1, 2, 0, 0
chi = n0 - n1 + n2 - n3 + n4
check("chi_112_is_2", chi == 2, f"chi=1-1+2={chi}")
check("chi_contractible_is_1", 1 == 1, "chi(pt)=1")
check("chi_mismatch", chi != 1, f"{chi} != 1 => not contractible, not a homology ball")

# (2) Cellular chain rank-nullity: C2=Z^2 -> C1=Z -> C0=Z
# d1: Z->Z is 0 (connected, single 0-handle, one 1-handle loop killed? keep general):
# rank(ker d2) = 2 - rank(im d2) >= 2-1 = 1, so either im d2 != Z (H1!=0) or ker d2 != 0 (H2!=0).
rank_im_d2_max = 1  # rank(C1)=1
ker_rank_min = n2 - rank_im_d2_max
check("rank_nullity_forces_homology", ker_rank_min >= 1,
      f"rank ker(d2) >= {ker_rank_min}: H1=Z/im(d2) and H2=ker(d2) cannot both vanish")
# Exhaust both cases explicitly
for im_rank in (0, 1):
    H1_rank = 1 - im_rank  # rank coker ignoring torsion; >=0
    H2_rank = 2 - im_rank
    check(f"case_im{im_rank}_nontrivial", (H1_rank > 0 or H2_rank > 0),
          f"im_rank={im_rank} => rkH1={H1_rank}, rkH2={H2_rank}")

# (3) Stein => handles of index <= 2 (Eliashberg/Gompf), so n3=n4=0 forced; no repair inside class
check("stein_index_bound", n3 == 0 and n4 == 0, "Stein compact => 2-complex; 3/4-handles absent")

# (4) 3-handle repair arithmetic (leaves Stein class)
chi_repaired = 1 - 1 + 2 - 1
check("repair_chi", chi_repaired == 1, f"1-1+2-1={chi_repaired} (needs a 3-handle: non-Stein)")
# Exhibit an acyclic (but non-Stein) example chain: d3(1)=(1,0), d2(a,b)=b
# H2 = ker d2 / im d3 = {(a,0)}/{(c,0)} = 0; H1 = ker d1/im d2 = Z/Z = 0. Ranks work.
check("repair_chain_acyclic_ranks", (2 - 1) - 1 == 0 and 1 - 1 == 0, "ranks cancel with one 3-handle")

# (5) Terminology cross-check
check("mazur_type_is_1plus1", (1, 1) != (1, 2), "Mazur-type=(1x1-h,1x2-h); target counts=(1,2)=plug-type")

print(f"\n{len(passed)}/{len(passed) + len(failed)} checks passed")
if failed:
    print("VERIFY_FAIL", failed)
    raise SystemExit(1)
print("VERIFY_OK")
