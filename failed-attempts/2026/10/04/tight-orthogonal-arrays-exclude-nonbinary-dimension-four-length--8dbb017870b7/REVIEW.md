# Independent mathematical audit

## correctness

PASS

A length-maximal \(k=4,s=q-1\) code has \(n=q^2+q+2\), \(d=q^2\), and \(q^4\) words. Alderson's equality theory gives orthogonal-array strength at least \(k-1=3\). For these parameters Rao's strength-three bound is met with equality: \(1+n(q-1)+(n-1)(q-1)^2=q^4\). Noda's complete theorem for Rao-tight strength-three arrays permits only the binary family \(\operatorname{OA}(2n,n,2,3)\) with \(4\mid n\), or \(\operatorname{OA}(q^3,q+2,q,3)\) with even \(q\). The candidate \(\operatorname{OA}(q^4,q^2+q+2,q,3)\) fits neither family for \(q\ge3\). For \(q=2\), the extended binary Hamming code gives the stated witness.

## originality

FAIL

The final nonexistence is already a direct consequence of two published theorems. Alderson explicitly states that every length-maximal integer-dimension code is an orthogonal array of strength at least \(k-1\), and isolates \(k=4,s=q-1\) as a surviving parameter branch. Noda's Theorem 1 completely classifies every strength-three orthogonal array attaining Rao's bound. Substituting the forced Alderson parameters into Rao's equality and then into Noda's two families immediately eliminates every \(q\ge3\). Thus the coding statement is a short corollary of existing coverage even though neither paper uses the assigned title.

## value

FAIL

The eliminated branch is mathematically natural, but once Alderson's orthogonal-array reduction and Noda's complete tight-array classification are placed side by side, the conclusion is a routine parameter corollary. Under the common value bar, this does not constitute an independent structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
