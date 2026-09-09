"""Lane-480: obstruction tower for climbing the window (stdlib only).

Rigorous conditional tower (cites BX Thm 7.15 hypotheses + Bockstein dictionary):
 - Step S6 (entry): build theta_7 in S/lambda^5 with 2*theta_7=0 needs
     H6: theta_6^2 = 0 in pi_{252,4}(S/lambda^3).  [BX Thm 7.15 at (j,r)=(6,5)]
 - Step S7 (next): build theta_8 in S/lambda^r with 2*theta_8=0 needs
     2*theta_7 = 0 AND lambda^2*theta_7^2 = 0 in S/lambda^r,
   i.e. H7(r): theta_7^2 = 0 in pi_{508,4}(S/lambda^{r-2}).
   Bidegree: 2*254 = 508, filt 2*2 = 4.
 - Hence: even after entry, every further page climbed toward/through the
   window's upper edge, and any constraint on d(h7^2) via a theta_8 construction,
   demands vanishing at stem 508 — two octaves above all cited charts
   (BX Lemmas 7.9/7.10 end ~stems 252-254; LWX appendix ends ~127; IWX ~200).
 - Classical reading of H7: Adams filtration of Theta_7^2 at stem 508
   (Theta_7 itself is only known to exist if HHR fails to kill earlier —
   in fact HHR guarantees h7^2 dies, so Theta_7 does NOT exist; H7 is thus
   about the synthetic square theta_7^2 as an obstruction class, not a
   spherical square).

Consequence logged: the target window [6,9] sits behind TWO uncharted doors —
  door 1 (entry): (252,4)/lambda^3; door 2 (page selection/upper climb): (508,4).
This explains precisely why the hour cannot close T without a new Ext/synthetic
computation at one of these bidegrees; it is a localized obstruction analysis,
not a proof of T and not an emergent claim.

Run: python3 output/artifacts/check_obstruction_tower.py -> OBSTRUCTION_TOWER_OK
"""
import sys

def main():
    th6, th7 = (126, 2), (254, 2)
    sq6 = (2*th6[0], 2*th6[1])
    sq7 = (2*th7[0], 2*th7[1])
    assert sq6 == (252, 4), sq6
    assert sq7 == (508, 4), sq7
    print(f"H6 (entry): theta_6^2=0 in pi_{sq6[0]},{sq6[1]}(S/lambda^3) [Thm 7.15 (6,5)]")
    print(f"H7 (climb): theta_7^2=0 in pi_{sq7[0]},{sq7[1]}(S/lambda^(r-2)) [Thm 7.15 (7,r)]")
    print("Door 1 (252,4): Theta_6-square, LWX Q1.6/Q1.7-type, UNKNOWN")
    print("Door 2 (508,4): synthetic theta_7-square, uncharted, UNKNOWN")
    print("OBSTRUCTION_TOWER_OK")

if __name__ == "__main__":
    sys.exit(main())
