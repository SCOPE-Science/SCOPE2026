# Independent mathematical audit

## correctness

PASS

The ordered seven-vertex complex is the d=2 case of the closed combinatorial manifold theorem, and the earlier connectivity/homology theorem gives simple connectivity and integral middle rank 40. I independently triangulated the product cells by monotone staircases. Replay: python3 /workspace/evidence/deleted_product_staircases.py. It produces simplex counts (42,420,1680,2100,840), verifies the signed simplicial fundamental cycle and the reversing coordinate swap, and checks ordinary simplicial Alexander–Whitney self-cups on all 419 basis cocycles of the kernel of the degree-two coboundary, with coboundary rank 379. Thus all mod-two self-cups vanish, and Wu and Poincaré duality give w2=0 and evenness. The signed swap gives signature zero; integral Poincaré duality, even indefinite unimodular lattice classification and Freedman's theorem (the combinatorial structure gives Kirby–Siebenmann invariant zero) then give exactly the stated TOP type. In the supplied checker line 147 uses (-1)^(3+i) rather than (-1)^(2+i); this flips the entire (3,2) cardinality sector of the boundary rows and does not change the zero test, since first-factor faces land in the disjoint (2,3) sector. The independent simplicial computation uses actual simplicial boundary signs. No PL or smooth classification follows.

## originality

FAIL

A distinct catalog record gives the identical ordered complex, spin, signature zero, H^20 and TOP #20(S²×S²), and gives a closely related mod-two cup-square proof. The difference in the choice of orientation-reversing symmetry and cohomology computation does not distinguish the finding. The two records' shared date does not determine who obtained the result first; the failure is demonstrable equivalent coverage, not an inference of precedence or lack of independence.

## value

PASS

The actual invariant is mathematically useful: homology alone does not distinguish even and odd intersection forms, and the exact form resolves the four-dimensional case of a stated configuration-space conjecture and yields the TOP type. This is the value of the mathematical result, not a distinct contribution over the covering record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
