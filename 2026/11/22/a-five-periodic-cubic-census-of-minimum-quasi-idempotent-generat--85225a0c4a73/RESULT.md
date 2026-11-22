# A five-periodic cubic census of minimum quasi-idempotent generating systems

## Finding

Let \(\mathcal O_n\), for \(n\ge4\), be the semigroup of singular nondecreasing full transformations of the chain \([n]\), and let a *strict quasi-idempotent* mean \(f\ne f^2=f^4\). Denote by \(M_n\) the number of distinct **unordered subsets** of strict quasi-idempotents that generate \(\mathcal O_n\) and have minimum possible cardinality. If \(n=5k+r\) with \(0\le r<5\), then for all \(n\ge5\),

\[
M_n=\begin{cases}
(2k-1)(2k^2+4k-3)/3,&r=0,\\
1,&r=1,\\
k(2k+1),&r=2,\\
2k,&r=3,\\
2k+1,&r=4.
\end{cases}
\]

At the remaining boundary \(n=4\), \(M_4=1\). In particular, **there is a unique minimum generating subset for every \(n\equiv1\pmod5\)** (\(n\ge6\)). The minimum cardinality, already established in the cited 2026 work, is \(q_n=\lfloor6n/5\rfloor-\mathbf1_{n\equiv1\pmod5}\); the assertion here is the complete *multiplicity* classification, not a new claim for \(q_n\).

## Assumptions and scope

All functions have domain and codomain \([n]\), are nondecreasing, and are nonbijective. A generator of rank \(n-1\) is uniquely indexed by its collapsed adjacent input pair \(i,i+1\) and omitted output \(j\), written \(e_{i,j}\). All strict quasi-idempotents of rank \(n-1\) are \(e_{i,i-1}\), for \(2\le i\le n-1\), and \(e_{i,i+2}\), for \(1\le i\le n-2\). This characterization and the exact minimum cardinality are established in the references; lower-rank quasi-idempotents cannot appear in a minimum generating set since a full top-rank generating set is necessary.

## Proof

**Generating criterion.** The cited exact-rank paper proves that a selection of these \(2(n-2)\) candidate elements generates precisely when every input-collapse row and every omitted-output column is covered and the directed incidence graph crosses every proper initial-segment cut both ways. Its proof shows sufficiency by sink-component intervals; these are necessary and sufficient constraints rather than heuristic degree conditions. We use that published criterion here, without reasserting its novelty.

**Sixteen-state weighted transfer.** For \(1\le i\le n-2\), let \(l_i\) indicate selection of \(e_{i,i-1}\), and let \(r_i\) indicate selection of \(e_{i,i+2}\). At \(i=1\), the only candidate is \(r_1\), which must equal one. For \(2\le i\le n-2\), a permitted choice \((l_i,r_i)\) is one of \((0,1),(1,0),(1,1)\). The generating criterion is equivalent, inductively, to the three tests

\[
l_{i-1}\lor l_i,\qquad r_{i-1}\lor r_i,\qquad l_i\lor r_{i-3};
\]

where the missing initial \(r_{-1},r_0\) are zero. Equivalently, after processing position \(i-1\), encode \((l_{i-1},r_{i-1},r_{i-2},r_{i-3})\) as one of sixteen binary states. An arc to \((l_i,r_i,r_{i-1},r_{i-2})\) is allowed exactly when the three displayed tests hold, of weight \(l_i+r_i\). At the last processed index \(i=n-2\), require \(r_i=r_{i-1}=1\) and add one for the forced final left generator \(e_{n-1,n-2}\). This yields a finite exact counting recurrence with no missing end cases.

**Exact count-vector certificate.** Let \(D_i(s)=(c_i(s),a_i(s))\) record the minimum number of selected candidates along paths reaching state \(s\) and the number of such minimum-cost paths. Extend by each allowed arc: retain the least cost and add multiplicities over all ties. Initialize at \(i=1\) with state \((0,1,0,0)\) of cost one and multiplicity one. At indices \(i=5j+4\) (\(j\ge0\)) precisely eight states are reachable with finite minimal cost, in the following order:

\[
(0101),(0110),(0111),(1010),(1011),(1101),(1110),(1111).
\]

Their cost vector is \((5,5,6,5,6,6,6,7)+6j\). Their multiplicity vector is

\[
(2j+1,1,2j+1,2j+1,E_j,(j+1)(2j+1),2j+1,E_j),
\quad E_j=(2j+1)(2j^2+8j+3)/3.
\]

At \(j=0\), this follows from exactly three finite transfer steps. Applying **five further transfer steps** to this vector produces the same formulas at \(j+1\). This is a finite algebraic identity, not a numerical extrapolation: the minimum-cost tie choices depend only on the eight constant cost offsets, and the resulting multiplicities are fixed linear combinations of the input polynomials of degree at most three. Consequently verifying the five-step identity at four integer values of \(j\) proves it as a polynomial identity for all \(j\). `checker.py` checks each of those four exact cases and the cost offsets, and independently checks many further values. Thus induction establishes the displayed vector for every \(j\ge0\).

From \(i=5j+4\), apply zero, one, two, three, or four more transfer steps, add the mandatory final generator, and select only terminal states with the two newest right indicators equal to one. The minimum-cost output multiplicities are respectively

\[
1,\quad(j+1)(2j+3),\quad2(j+1),\quad 2j+3,\quad E_{j+1}.
\]

These correspond to \(n=5j+6,\ldots,5j+10\), exactly the five residue formulas after substituting \(k=j+1\) or \(k=j+2\). The two cases \(n=4,5\) are determined directly by the same finite transition, with a single minimum subset in each case. The indicated minimum costs agree with the previously proved exact quasi-idempotent rank \(q_n\). Therefore the enumerated subsets are exactly all the minimum generating subsets. This completes the proof.

## Verification

`checker.py` is standalone Python 3 code using integer arithmetic only. It builds all sixteen states and legal transitions, confirms the initial cost/multiplicity vector, checks the five-step polynomial identity at four values (sufficient by the degree argument), checks all five terminal multiplicity identities, and independently evaluates the full dynamic programme through \(n=60\), including \(n=4,5\). These finite certificate checks supplement the algebraic induction; the proof of the infinite assertion is the verified finite transition identity plus the polynomial-degree argument.

## Relationship to prior work

Imam, Ibrahim, Garba, Usman and Idris (2023) characterize rank-\(n-1\) quasi-idempotents and give an upper bound for their generating rank. The October 2026 paper *Exact quasi-idempotent generating rank of the singular order-preserving transformation semigroup* proves the exact minimum cardinality and the necessary-and-sufficient incidence criterion used above. Its Limitations section explicitly leaves open the total number of distinct minimum generating subsets, which is determined here. Its transfer-matrix idea provides the starting point, but the cubic residue-dependent multiplicities and uniqueness phenomenon are additional assertions.

## Limitations

The theorem counts distinct *unlabelled-as-sets* generating subsets, not ordered sequences, nonminimal generating sets, or arbitrary partial transformation semigroups. The proof relies on the published incidence-generation criterion; it does not independently rederive all semigroup factorization facts. Novelty is assessed relative to the inspected primary literature, accessible prior records, and indexed mathematical search; an unindexed older equivalent enumeration remains possible.

## References

1. A. T. Imam, S. Ibrahim, G. U. Garba, L. Usman, A. Idris, *Quasi-idempotents in finite semigroup of full order-preserving transformations*, Algebra and Discrete Mathematics **35** (2023), 62–72, DOI: 10.12958/adm1846. https://admjournal.luguniv.edu.ua/index.php/adm/article/download/1846/pdf
2. *Exact quasi-idempotent generating rank of the singular order-preserving transformation semigroup*, published mathematical finding (12 October 2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-exact-quasi-idempotent-generating-rank-of-the-singular-order-pre--da3148498843/RESULT.md
