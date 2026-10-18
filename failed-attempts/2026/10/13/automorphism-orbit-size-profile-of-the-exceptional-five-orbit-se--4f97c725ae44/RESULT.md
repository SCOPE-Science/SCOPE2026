# Automorphism-orbit size profile of the exceptional five-orbit semidirect product

## Finding
Let \(V=(\mathbb F_{16},+)\). Choose \(\zeta\in\mathbb F_{16}^{\times}\) of order \(5\), and let
\[
D_{10}=\langle a,t\mid a^5=t^2=1,\;tat=a^{-1}\rangle
\]
act on \(V\) by
\[
a(v)=\zeta v,\qquad t(v)=v^4.
\]
For \(G=V\rtimes D_{10}\), the five \(\operatorname{Aut}(G)\)-orbits have sizes
\[
1,\;15,\;64,\;20,\;60.
\]
They are, respectively, \(\{1\}\), \(V\setminus\{0\}\), \(G'\setminus V\), the involutions in \(G\setminus G'\), and the elements of order \(4\) in \(G\setminus G'\). In particular, the involutions split into exactly two automorphism orbits, of sizes \(15\) and \(20\).

## Assumptions and scope
The dihedral notation here has \(|D_{10}|=10\). The field \(\mathbb F_{16}\) is viewed additively as a four-dimensional vector space over \(\mathbb F_2\). Since \(\operatorname{ord}_5(2)=4\), multiplication by an element of order \(5\) is irreducible on this vector space. The Frobenius map \(v\mapsto v^4\) has order \(2\) and sends \(\zeta\) to \(\zeta^{-1}\), so the displayed formulas define the required \(D_{10}\)-action.

The result concerns this explicit semidirect product, which is the exceptional non-\(S_4\) group singled out in the Fitting-height-three part of Kato's classification.

## Proof
Write \(H=\langle a,t\rangle\cong D_{10}\). First, \(V=O_2(G)\): the image in \(H\) of any normal \(2\)-subgroup of \(G\) is a normal \(2\)-subgroup of \(D_{10}\), hence trivial. Thus \(V\) is characteristic. Also
\[
G'=V\rtimes\langle a\rangle.
\]
Indeed, \(H'=\langle a\rangle\), while \([V,\langle a\rangle]=V\) because multiplication by \(\zeta-1\) is invertible. Hence \(G'\) is characteristic.

These characteristic subgroups and element orders give five pairwise disjoint \(\operatorname{Aut}(G)\)-invariant subsets:
\[
\{1\},\quad V^{\#},\quad G'\setminus V,\quad
\{g\in G\setminus G':|g|=2\},\quad
\{g\in G\setminus G':|g|=4\}.
\]
Their sizes can be obtained directly. The first two have sizes \(1\) and \(15\). Every element in a coset \(Va^i\) with \(1\le i\le4\) has order \(5\), because \(a^i\) acts fixed-point-freely and
\[
1+a^i+(a^i)^2+(a^i)^3+(a^i)^4=0
\]
as an endomorphism of \(V\). Thus \(|G'\setminus V|=4\cdot16=64\).

There are five reflections in \(D_{10}\). For a reflection \(r\) and \(v\in V\),
\[
(vr)^2=v+r(v).
\]
The fixed space of \(t:v\mapsto v^4\) is \(\mathbb F_4\), of size \(4\), and all reflections are conjugate. Hence each reflection coset contains exactly \(4\) involutions and \(12\) elements of order \(4\). This gives \(5\cdot4=20\) and \(5\cdot12=60\).

It remains to show that none of these invariant subsets splits further under automorphisms. This is certified by an exhaustive computation in the explicit four-dimensional binary model. All
\[
|\operatorname{GL}_4(2)|=(16-1)(16-2)(16-4)(16-8)=20160
\]
invertible binary matrices are enumerated. Exactly \(60\) normalize the displayed linear copy of \(D_{10}\). Together with all \(16\) translations they give \(960\) affine normalizers of \(G\), and conjugation by these normalizers produces exactly five orbits on the \(160\) elements of \(G\), with sizes \(1,15,20,60,64\). Because the five subsets above are invariant under the full automorphism group, these affine-normalizer orbits cannot be fused by any further automorphism. Reordering them by the displayed description yields \(1,15,64,20,60\).

## Verification
The accompanying `verify.py` implements \(\mathbb F_{16}=\mathbb F_2[u]/(u^4+u+1)\), takes \(\zeta=u^3\), reconstructs the two generators of \(D_{10}\), enumerates every element of \(\operatorname{GL}_4(2)\), finds the complete linear normalizer, and then computes the induced affine-normalizer conjugacy orbits on all \(160\) group elements. It additionally checks the element orders and membership in \(V\) and \(G'\) for each orbit. The expected terminal line is `CHECK_OK`.

The finite computation is exhaustive: there is no sampling or search cutoff. The structural argument using \(O_2(G)\), \(G'\), and element order explains why the subgroup orbits computed by the affine normalizer are already the full automorphism orbits.

## Relationship to prior work
Kato classifies the solvable non-prime-power groups with five automorphism orbits. In Fitting height \(3\), the two possibilities are \(S_4\) and \(C_2^4\rtimes D_{10}\), with the \(C_5\)-subgroup acting irreducibly on \(C_2^4\). The paper also proves that, in this case, the nonzero Fitting subgroup and the next characteristic layer are each single automorphism orbits, and that the complement-side part splits into two orbits. It does not state the orbit cardinalities \(1,15,64,20,60\).

The earlier paper of Laffey and MacHale initiates the finite automorphism-orbit classification and treats groups with at most four orbits; it does not cover this five-orbit group. Targeted searches for the explicit semidirect product together with the orbit-size tuple did not locate an earlier statement of this profile.

## Limitations
The claim is only the orbit-size profile for this particular order-\(160\) semidirect product. It does not classify automorphism-orbit sizes for all five-orbit groups, and it does not compute the full abstract automorphism group. The proof only needs a sufficiently large explicitly enumerated subgroup of \(\operatorname{Aut}(G)\), namely the conjugation action of the affine normalizer, because characteristic-subgroup and order invariants prevent any further fusion.

## References
1. J. Kato, *Finite Non-\(p\)-Groups with 5 Automorphism Orbits*, arXiv:2610.00786v1, 2026.
2. T. J. Laffey and D. MacHale, *Automorphism orbits of finite groups*, J. Austral. Math. Soc. Ser. A 40 (1986), 253–260, doi:10.1017/S1446788700027221.
