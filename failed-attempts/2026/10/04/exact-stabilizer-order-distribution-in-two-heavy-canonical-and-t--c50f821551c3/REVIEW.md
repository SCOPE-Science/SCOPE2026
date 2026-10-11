# Independent mathematical audit

## correctness

PASS

The gcd scaling and triangular count are correct. Fixing \(g=\gcd(a,b)\) and writing \(a=gc\), \(b-a=ge\) turns the canonical region into the primitive two-heavy triangle with radius \(R=\lfloor r/g\rfloor\), and the terminal region into the same triangle with \(R=\lfloor(r-1)/g\rfloor\). The primitive count is \(3\Phi(R)\). Fresh enumeration at \(r=2,3,5,10\) reproduced every per-g count.

## originality

FAIL

The final formulas are a direct rescaling corollary of two already published SCOPE results. The published triangular classification gives exactly the canonical/terminal parameter triangles. The published totient census proves both that the generic heavy-line stabilizer is governed by gcd(a,b) and that primitive points in those triangles are counted by \(3\Phi(R)\) and \(3\Phi(R-1)\). After fixing gcd g, division by g literally replaces r by \(\lfloor r/g\rfloor\) (or \(\lfloor(r-1)/g\rfloor\)); no new structural lemma is needed. This prior implication decisively covers the claimed all-g distribution.

## value

FAIL

Although the stabilizer distribution is a natural way to package the data and the formulas are correct, obtaining it requires only fixing gcd g, dividing by g, and applying the already published primitive-triangle count at a smaller radius. Under the stated value standard this is a renaming/rescaling substitution rather than a new motivated structural result, classification, or non-implied invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
