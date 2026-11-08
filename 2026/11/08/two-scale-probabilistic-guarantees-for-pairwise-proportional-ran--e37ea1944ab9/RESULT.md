# Two-scale probabilistic guarantees for pairwise-proportional ranking compression

## Finding

Consider \(n\ge2\) independent uniformly random strict rankings of \(m\ge2\) alternatives (impartial culture). Compress them into exactly two possibly synthetic strict rankings under pairwise proportionality as defined below. Write \(G\) for the undirected graph joining two alternatives if **all** input rankings order that pair identically, and \(X=|E(G)|\).

**Theorem.** For every input profile whose unanimous-comparison graph \(G\) is a matching, a deterministic block-reversal construction produces two pairwise-proportional output rankings. Consequently, at every \(n,m\),
\[
\Pr(\text{pairwise-proportional compression exists})\ge 1-\binom m3\bigl(6\cdot3^{-n}-6\cdot6^{-n}\bigr).
\]
In particular, pairwise-proportional compression exists with probability tending to one whenever \(m=o(3^{n/3})\).

The simpler construction consisting of a ranking and its literal reverse is pairwise proportional **if and only if** \(X=0\). If \(m/2^{n/2}\to c\) for fixed \(0<c<\infty\), then
\[
X\xrightarrow{d}\operatorname{Poisson}(c^2),\qquad
\Pr(\text{a literal-reversal compression succeeds})\longrightarrow e^{-c^2},
\]
whereas the block-reversal construction succeeds with probability tending to one on the very same scale. Thus the nontrivial literal-reversal transition does not indicate a genuine loss of pairwise-proportional representability.

## Assumptions and scope

There are \(n\) voters and \(m\) labeled alternatives; each input ranking is chosen independently and uniformly from all \(m!\) complete strict orders. Two **synthetic** output rankings are permitted, as in Halpern et al. Each ordered alternative pair \((a,b)\) must appear in at least \(t\) of the two output orders whenever at least \(tn/2\) of the input orders place \(a\) above \(b\), for each \(t\in\{1,2\}\). Thus a unanimously oriented pair must have the same orientation in both outputs; every nonunanimous pair is adequately covered if the two outputs order it oppositely. No result is asserted for \(k\ne2\), for correlated or nonuniform input rankings, or for arbitrary finite profiles with a nonmatching unanimous graph.

## Proof

**1. Exact finite construction.** For each edge \(\{a,b\}\) of the matching \(G\), form a two-alternative block ordered internally according to the unanimous preference; every unused alternative is a singleton block. Choose any ordering of these blocks. The first output concatenates the blocks in this order, and the second concatenates the blocks in the *reverse block order*, without reversing the order within each block. Every unanimous pair lies inside its two-alternative block and is oriented the required way in both outputs. Every pair from different blocks appears in opposite orders in the two outputs. A nonunanimous comparison never requires both output rankings to agree; at most one comparison-direction requirement per ordered pair may demand an output, and opposite output orientations satisfy all such demands, including exact half/half input ties. Hence both outputs satisfy pairwise proportionality. A literal ranking and its full reverse can meet a unanimous pair in at most one of the two outputs, so it works precisely when there are no unanimous pairs; if none exist it covers both orientations of every pair.

**2. Exact probability of overlapping unanimity edges.** Fix three alternatives \(a,b,c\). The event that at least two of their three undirected comparison pairs are unanimous is the union of the six events saying that one specified alternative is unanimously above both other alternatives, or unanimously below both. Each event has probability \(3^{-n}\), because a specified alternative is extreme among these three in each independent voter ranking with probability \(1/3\). Any two of the six events can both occur only when all \(n\) rankings induce the identical order on the triple; there are six such orders, each having probability \(6^{-n}\), and each belongs to exactly two extreme events. Therefore the exact triple probability is
\[
q_n=6\cdot 3^{-n}-6\cdot 6^{-n}.
\]
If a simple graph fails to be a matching then some triple supports two incident edges. A union bound over the \(\binom m3\) triples gives \(\Pr(G\text{ is not a matching})\le\binom m3 q_n\). This proves the finite lower bound. It tends to zero whenever \(m^3 3^{-n}\to0\), equivalently \(m=o(3^{n/3})\).

**3. Poisson law for the mirror threshold.** For each candidate pair \(e\), let \(I_e\) indicate unanimous comparison. Then
\[
p_n=\mathbb E I_e=2^{1-n},\qquad \lambda_{n,m}=\mathbb E X=\binom m2 2^{1-n}.
\]
Events indexed by disjoint candidate pairs are jointly independent of the entire collection of indicators formed without those two candidates: in each uniform ranking, the internal relative order of two specified candidates is independent of the relative order restricted to the other \(m-2\) candidates. Hence the line graph of the complete graph gives a valid dependency graph for \(\{I_e\}\). Two distinct candidate pairs sharing one vertex satisfy
\[
\mathbb E(I_eI_f)=2\cdot3^{-n}+2\cdot6^{-n}=:r_n,
\]
by partitioning into the four possible unanimous orientations of their two comparisons: their shared candidate is unanimously at the top or bottom (each probability \(3^{-n}\)), or unanimously in the middle in one of two orders (each probability \(6^{-n}\)). By the standard dependency-neighborhood Chen--Stein Poisson approximation theorem of Arratia, Goldstein and Gordon,
\[
d_{\mathrm{TV}}(\mathcal L(X),\operatorname{Poisson}(\lambda_{n,m}))
\le 2\left[\binom m2(2m-3)p_n^2+\binom m2(2m-4)r_n\right].
\]
When \(m/2^{n/2}\to c\in(0,\infty)\), \(\lambda_{n,m}\to c^2\); the two error terms vanish, since \(m^3 4^{-n}\to0\) and \(m^3 3^{-n}\to0\) (using \(2^{3/2}<3\)). Hence \(X\) converges in total variation to the specified Poisson distribution. The equivalence between literal-reversal success and \(X=0\) gives its limiting probability. Finally \(2^{n/2}=o(3^{n/3})\) because \(\sqrt 2<\sqrt[3]3\), so Step 2 simultaneously proves block-reversal success with probability \(1-o(1)\).

## Verification

Run `python verify.py` using Python 3 standard library only. This exhaustively enumerates \(14{,}652\) labeled input-ranking profiles across \((m,n)=(3,2),(3,3),(4,2),(4,3)\), checks the exact matching/block-reversal implication and the literal-reversal criterion, and separately checks the two exact three-alternative probability identities for \(2\le n\le5\). The universal result and asymptotic conclusion follow from the proof above, not the finite experiments. The dependency-neighborhood Poisson approximation bound is an explicitly identified standard published theorem rather than an unverified computational step.

## Relationship to prior work

Halpern, Liu, Micha, Ng and Suksompong (2026, arXiv:2610.23193, first posted October 16, 2026) introduced pairwise proportionality in ranking compression. Their Theorem 3 proves impossibility on certain adversarial profiles; Theorems 4 and 5 establish existence on single-peaked and single-crossing domains. Section 6 specifically raises probabilistic existence guarantees as a future research direction. The present result considers independent uniformly random input rankings rather than those structured domains and provides an explicit synthetic two-ranking construction with a quantitative high-probability bound even when the number of alternatives grows exponentially in the electorate size. The Chen--Stein dependency-neighborhood approximation is a standard probabilistic tool, not claimed as new.

## Limitations

The finite lower bound is a sufficient condition, not an exact probability of general pairwise-proportional existence; profiles with overlapping unanimous edges may still admit valid output rankings. The scale \(3^{n/3}\) is an achieved growth regime, **not** a proved sharp threshold for solvability. The \(2^{n/2}\) Poisson window is sharp only for the literal-reversal construction. Impartial-culture independence is essential to the probability calculation. No claims are made about empirical preferences, arbitrary input correlations, or independent validation.

## References

1. Daniel Halpern, Xinyu Liu, Evi Micha, Yu Peng Ng and Warut Suksompong. *Proportionality in Ranking Compression*. arXiv:2610.23193 (first version October 16, 2026), especially Sections 5--6 and Theorems 3--5. https://arxiv.org/abs/2610.23193 ; openly available full text: https://daniel-halpern.com/files/proportional-compression.pdf
2. Richard Arratia, Larry Goldstein and Louis Gordon. *Two moments suffice for Poisson approximations: the Chen--Stein method*. Annals of Probability **17** (1989), 9--25. https://doi.org/10.1214/aop/1176991491
