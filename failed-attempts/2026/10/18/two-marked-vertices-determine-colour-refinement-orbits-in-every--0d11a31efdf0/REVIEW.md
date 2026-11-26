# Independent mathematical audit

## correctness

PASS

The theorem holds under the stated q≥3, d≥1 and distinctly named-anchor assumptions. Symbol relabellings and coordinate permutations normalize the anchors; the subgroup preserving equal and unequal coordinate blocks is transitive at fixed (s,r,t). A uniquely marked vertex's distance layers are determined by the refinement colours by round d, by induction on distance. In the next round the count of neighbours decreasing both distances is precisely s: a simultaneous decrease needs a replacement by the common anchor symbol. Then r=s+b−dist(x,u) and t=s+b−dist(x,v). Invariance under anchor-fixing automorphisms prevents splitting the triple classes and proves full orbit recovery and stability. Choosing the coordinate categories and their free symbols gives the stated sizes and class count, including a=0 and d=1. The explicit H(3,3) witness has distances (2,2) on both vertices and simultaneous-decrease counts 0 and 1. Independent exact refinement checked whole classes, sizes and T=s on 22 anchor cases and 1,084 vertex instances (q=3,d≤4; q=4,5,d≤3; all b). Largest observed depth was 3. Replay: python3 /workspace/branches/72b5ccc9-6b51-4cf6-a3fe-257f65dbda55/record5_reproduction.py. These tests corroborate rather than prove the universal statement. The original VERIFICATION.md and its two scripts/logs are finite evidence, not formal verification or attestation.

## originality

FAIL

A distinct Resultary record covers the same orbit classification, coordinate labels, nonbinary census and class sizes, and simultaneous-decrease statistic; it treats q≥2 and also gives the exact metric-pair obstruction. The frozen d+1 bound, though not explicitly given there from the three-colour initialization, follows mechanically by combining one-round repair from the distance-pair partition with ordinary distance propagation from the two named anchors. Coverage is demonstrated without attributing priority from the shared date.

## value

FAIL

The classification is useful as an explicit invariant, but the matching broader result already supplies it and the obstruction. The only apparent additional assertion is a nonsharp absolute bound obtained by appending the already-covered repair step to routine distance propagation. No independently useful new depth threshold or other mathematical contribution is established for this frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
