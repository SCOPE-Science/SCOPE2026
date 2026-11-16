# Exceptional six-vertex Walsh cancellations for cographs and a seven-vertex modular recovery law

## Finding

Let \(n\in\{4,5,6,7\}\) and let \(E_n=E(K_n)\). A *cograph* is a simple graph containing no induced four-vertex path \(P_4\). Define its binary edge-incidence indicator \(f_n:\mathbb F_2^{E_n}\to\{0,1\}\) and its **unnormalized** Walsh transform
\[
W_n(S)=\sum_{G\text{ a labelled cograph on }[n]}(-1)^{|E(G)\cap S|},\qquad S\subseteq E_n.
\]

**Theorem (complete cancellation classification through seven vertices).** For every \(n\in\{4,5,6,7\}\), \(W_n(S)=0\) whenever \(|S|\) is odd. For \(n=4,5,7\), these are *all* the zeros. For \(n=6\), the only additional zeros have even support and are precisely the two relabelling families
\[
S=E(K_6)\setminus E(P_4\sqcup 2K_1)\quad(180\text{ supports}),
\qquad
S=E(K_6)\setminus E(C_5\sqcup K_1)\quad(72\text{ supports}).
\]
Thus the four ranks of counting convolution by \(f_n\), in order \(n=4,5,6,7\), are \(32,512,16132,1048576\). The corresponding smallest positive absolute Walsh multipliers are \(4,8,16,16\).

The seven-vertex assertion has the stronger uniform modular form
\[
\boxed{W_7(S)\equiv16\pmod{32}\quad\text{whenever }|S|\text{ is even}.}
\]
In particular every even-support Fourier mode is recoverable at seven vertices, despite the two unexpected six-vertex cancellation families.

## Assumptions and scope

All graphs are simple, undirected, **labelled** on \([n]\). The Fourier group is the additive Boolean edge cube \(\mathbb F_2^{\binom n2}\), *not* the space of unlabelled graphs. The indicator takes value one at exactly the cographs and zero elsewhere. The transform is unnormalized, with characters \(\chi_S(x)=(-1)^{\langle S,x\rangle}\). The counting-convolution operator is \((T_nh)(x)=\sum_y f_n(y)h(x-y)\). Its eigenvalues, and therefore its rank, are exactly the Walsh multipliers above.

The four cograph counts are respectively \(52,472,5504,78416\). The frequency-space sizes are respectively \(64,1024,32768,2097152\). No statement for \(n\ge8\) is made.

## Proof

**1. Forced cancellation.** Since \(P_4\) is self-complementary, graph complementation preserves cographs. For the all-ones edge vector \(\mathbf 1\), change variables \(G\mapsto\overline G\) to obtain
\[
W_n(S)=(-1)^{|S|}W_n(S).
\]
Hence odd-support frequencies vanish in every dimension. This is the *only* abstract symmetry argument used; it does not explain the even-support exceptions at six vertices.

**2. Seven-vertex modular certificate.** For an edge set \(T\), write
\[
N_7(T)=\#\{G\text{ labelled cograph on }[7]:T\subseteq E(G)\}.
\]
Expanding the character product yields the exact identity
\[
W_7(S)=\sum_{T\subseteq S}(-2)^{|T|}N_7(T).
\]
The standalone `cograph_mod32.cpp` uses the recursive union/join characterization and checks *every* possible \(T\subseteq E(K_7)\) with \(|T|\le4\). Its exhaustive integer certificate is
\[
\begin{aligned}
N_7(\varnothing)&=78416\equiv16\pmod{32},\\
N_7(T)&=39208\equiv8\pmod{16}&&(|T|=1),\\
N_7(T)&\equiv0\pmod{2^{5-|T|}}&&(2\le|T|\le4).
\end{aligned}
\]
There are respectively \(1,21,210,1330,5985\) tested edge patterns at sizes zero through four; all tests pass. Every term with \(|T|\ge5\) is divisible by \(32\). Therefore
\[
W_7(S)\equiv16-16|S|\pmod{32}.
\]
Even-support coefficients are congruent to \(16\) and cannot vanish; odd-support coefficients vanish exactly by Step 1. This proves the seven-vertex zero classification without extrapolating from a numerical sample.

**3. Six-vertex exceptional orbits and the small cases.** The finite certificate `cograph_fourier.cpp` examines each of the \(2^{\binom n2}\) labelled graphs for \(n=4,5,6,7\). It recognizes cographs by testing the induced graph on every four-set for the degree pattern \((1,1,2,2)\) with three edges. This pattern is exactly \(P_4\). It then applies the integer fast Walsh–Hadamard transform, whose butterfly \((a,b)\mapsto(a+b,a-b)\) is an exact evaluation of all characters.

The logically different `cograph_recursive.cpp` recognizes a cograph by recursively splitting disconnected components of the graph or its complement, until single vertices remain; if neither graph nor complement disconnects, it rejects. It independently computes the entire transform and at six vertices constructs the two proposed frequency orbits by applying every permutation in \(\mathfrak S_6\) to the complements of \(P_4\sqcup2K_1\) and \(C_5\sqcup K_1\). Its exact set equality check shows that **all** even-support zeros, and no others, are in these two orbits. The orbit sizes also follow directly as \(\binom64(4!/2)=180\) and \(6(5-1)!/2=72\).

The exact full-spectrum checks yield the following integer table (a program-generated **exhaustive finite** certificate, not an assumed all-order identity):

| \(n\) | Cographs | Odd-support zeros | Even-support zeros | Nonzero multipliers | Least nonzero magnitude |
|---|---:|---:|---:|---:|---:|
| 4 | 52 | 32 | 0 | 32 | 4 |
| 5 | 472 | 512 | 0 | 512 | 8 |
| 6 | 5504 | 16384 | 252 | 16132 | 16 |
| 7 | 78416 | 1048576 | 0 | 1048576 | 16 |

The recognition algorithms and every transformation use integer arithmetic; their independent results agree on each tested dimension. In particular, the six-vertex exceptional classification and the rank statements follow without a probabilistic error probability.

## Verification

From the directory containing the sources, run `sh CHECK.sh` using a C++17 compiler (`g++` recommended). This compiles and executes all three supplied standalone programs, including the complete seven-vertex modular certificate and the explicit six-vertex orbit-set equality test. The two recognition algorithms agree on all four labelled cograph counts and all Fourier rank/minimum summaries. `VERIFICATION.md` records the individual assertions and output signatures.

## Relationship to prior work

Ravelomanana and Thimonier established asymptotic enumeration of labelled and unlabelled cographs; Corneil, Perl and Stewart proved classical cograph recognition and cotree structure; Gioan and Paul provided a later decomposition-based recognition framework (arXiv first publicly posted 2008-10-10). Jones, Protti and Del-Vecchio developed linear-delay generation of *unlabelled* cographs (first publicly posted 2016-12-17). These sources establish the combinatorial family and practical recognition/generation methods, **not** the exact signed Walsh cancellation and orbit counts for labelled edge-incidence vectors. Ordinary cograph counts do not determine individual signed Fourier coefficients.

Related finite Fourier evaluations of different graph families (such as chordal-graph indicators and matching indicators) do not imply the present cograph statement: a chordal graph need not be a cograph, and a cograph need not be chordal (a four-cycle is a cograph). Complements of \(P_4\) and \(C_5\) are distinguished here as *frequency patterns*, not as forbidden-subgraph characterizations of the sampled graphs.

## Limitations

The seven-vertex congruence is proved by a fully specified finite low-moment certificate, not by an all-\(n\) symbolic formula. The six-vertex orbit classification is also finite and exhaustive. Neither a classification of zeros for \(n\ge8\) nor a prediction of future exceptional dimensions follows. Searches of accessible literature and indexed records cannot exclude unknown or unindexed earlier computations; the full text of Ravelomanana–Thimonier (2001) was not accessible, so the comparison with that source is abstract-level only. The mathematical proof has not undergone independent external audit.

## References

1. D. G. Corneil, Y. Perl and L. K. Stewart, “A Linear Recognition Algorithm for Cographs,” *SIAM Journal on Computing* **14** (1985), 926–934. DOI: https://doi.org/10.1137/0214065.
2. E. Gioan and C. Paul, “Split decomposition and graph-labelled trees: characterizations and fully-dynamic algorithms for totally decomposable graphs,” arXiv:0810.1823, first publicly posted 2008-10-10. https://arxiv.org/abs/0810.1823.
3. Á. A. Jones, F. Protti and R. R. Del-Vecchio, “Cograph generation with linear delay,” arXiv:1612.05827, first publicly posted 2016-12-17. https://arxiv.org/abs/1612.05827.
4. SageMath graph documentation, “Cographs,” https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/cographs.html (standard characterization and enumeration background).
5. V. Ravelomanana and L. Thimonier, “Asymptotic enumeration of cographs,” *Electronic Notes in Discrete Mathematics* **7** (2001), 58–61. DOI: https://doi.org/10.1016/S1571-0653(04)00224-0.
