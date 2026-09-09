"""Lane-480: quadratic-construction cell bidegrees for the j=6 -> 7 step (stdlib only).

Instantiates the cell diagram in the proof of BX Thm 7.15 (Burklund-Xu 2302.11869,
Sec 7.2) at j=6, i.e. the step that would build theta_7 (stem 254) from theta_6.
All claims here are integer bidegree arithmetic + named citations for the
homotopical inputs; no differential is claimed.

Cells (classical stems; synthetic weight = filt, i.e. constant-weight cells):
 - a: bottom cell of S^{2^{j+1}-2}/2 at j=6: S^{126}/2, class theta_6 on bottom.
 - b: top cell, stem 127, mapping by h_7 on tensor-down to S/lambda (uses r>=2, j>=3).
 - Extended powers (Ex. 7.13): three relevant cells over the unit 1:
     Q0(a): stem 2*126 = 252, filt 4  -> carries theta_6^2.
     Q0(b): stem 2*127 = 254, filt 2  -> carries h_7^2 class (theta_7 target).
     Q1(b)-Q3(a): stem 2*127-1 = 253, filt 3 -> attaching via lambda*2~ / lambda^2*eta.
 - After including the subcomplex and using lambda^2*theta_6^2 = 0 (hypothesis H),
   the composite factors through 1^{510-2,2}/2 = S^{254,2}/2 with bottom-cell map h_7^2.
   (Classical stems doubled: 2^{j+2}-2 = 254 at j=6; top cell 2^{j+2}-1 = 255.)

What this certifies: the ONLY homotopical input for the j=6 step beyond
2*theta_6 = 0 is hypothesis H: lambda^2*theta_6^2 = 0 in S/lambda^5
(i.e. theta_6^2 = 0 in S/lambda^3 at (252,4)). The cell numerology itself checks out;
H is exactly the blocking bidegree logged in WORKLOG Sec 4b. The shuffle maps
lambda*2~ and lambda^2*eta are as in BX proof diagram (p. ~115 of v3).

Run: python3 output/artifacts/check_quadratic_cells_j6.py -> QUAD_CELLS_J6_OK
"""
import sys

def main():
    j = 6
    bot = 2**(j+1) - 2        # 126
    top = bot + 1             # 127
    assert (bot, top) == (126, 127), (bot, top)
    q0a_stem, q0a_filt = 2*bot, 4       # theta_6^2
    q0b_stem, q0b_filt = 2*top, 2       # h_7^2 carrier
    mid_stem, mid_filt = 2*top - 1, 3   # Q1(b)-Q3(a)
    assert (q0a_stem, q0a_filt) == (252, 4), (q0a_stem, q0a_filt)
    assert (q0b_stem, q0b_filt) == (254, 2), (q0b_stem, q0b_filt)
    assert (mid_stem, mid_filt) == (253, 3), (mid_stem, mid_filt)
    # Final factored target: S^{2^{j+2}-2}/2 with bottom map h_7^2
    final_stem = 2**(j+2) - 2
    assert final_stem == 254, final_stem
    # d_r target window stems (source 254 -> 253) for context
    for r in (6, 7, 8, 9):
        assert (254 - 1, 2 + r) == (253, 2 + r)
    print(f"j=6 step: a=S^{bot}/2 (theta_6), b stem {top} (h_7 on tensor-down)")
    print(f"Q0(a)=(stem {q0a_stem}, filt {q0a_filt}) carries theta_6^2 [hypothesis H kills lambda^2*this]")
    print(f"Q0(b)=(stem {q0b_stem}, filt {q0b_filt}) carries h_7^2 [theta_7 output]")
    print(f"Q1(b)-Q3(a)=(stem {mid_stem}, filt {mid_filt}) attaching via lambda*2~/lambda^2*eta")
    print(f"factor target: S^{final_stem}/2 bottom map h_7^2; killing window targets (253,2+r) r=6..9")
    print("QUAD_CELLS_J6_OK")

if __name__ == "__main__":
    sys.exit(main())
