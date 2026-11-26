# Independent mathematical audit

## correctness

PASS

In an unrolled host, two consecutive weight-two windows t starts apart share the same residues for any retained ones modulo k; all deleted and entering positions lie in the same t-residue arc when t<k. With one retained one the distance changes by at most the arc diameter t-1; with none both distances are at most t-1; with both it is unchanged. For t>=k the bound is automatic. Cyclic variation between label extrema gives the claimed count of nonrequired windows. For the construction, neighboring gaps always sum to at least k, including the middle and cyclic join. Thus a gap d supports every allowed placement of the pair while the outside neighbors are excluded. The gaps sum to the claimed length. The N distinct windows require N starts, and 011 proves k=3. Independent exact small enumeration returned B2(3)=3, B2(4)=9, B2(5)=14, and direct extraction checked the construction for k=4..40: python3 /workspace/check_frozen_math.py. These are finite corroborations, not the proof. Frozen VERIFICATION.md and verify.py inspected but not executed.

## originality

FAIL

Two distinct published records establish the stronger exact answer B2(k)=binom(k,2)+k-1 for the identical freely padded cyclic problem for every k>=4. The decisive residual-circulation proof checks out: with at most k-2 extra edges, Fine–Wilf identifies any intersecting residual cycles, and each short cycle touching the adjacent-pair required component touches no other required component, so it cannot connect the required subgraph. Their periodic extra walk yields the same upper endpoint. A different explicit word and the elementary k=3 case do not give a surviving distinct covering theorem. This is verified coverage at review time, not a finding of earlier historical priority: both exact records are dated after the assigned record.

## value

PASS

The problem naturally asks how many nonrequired windows a cycle must pay to join rotation classes. Controlling the sharp linear correction, with a transparent variation obstruction and uniform construction, is mathematically substantive relative to the basic counting and weight-range bounds. The independent originality failure reflects supersession by the exact covering theorem, not a defect of motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
