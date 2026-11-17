# An exact last-defect rotor clock on triangular bouquets

## Finding

For every integer \(k\ge1\), let \(F_k\) consist of \(k\) vertex-disjoint pairs \((a_j,b_j)\) joined by triangles \(h,a_j,b_j,h\) around one common hub \(h\). Under the precisely specified single-chip rotor-router dynamics below, the first recurrence time is determined **only** by the last petal containing an initially directed two-cycle and the number of earlier such petals. The full first-entry-time generating polynomial is

\[
H_k(z)=3^k+\sum_{j=0}^{k-1}3^{k-1-j}z(z^4+3z^6)^j.
\]

The sharp time and exact number attaining it are

\[
\max_\rho\tau(\rho)=6k-5,\qquad
\#\{\rho:\tau(\rho)=6k-5\}=3^{k-1}.
\]

For independent uniformly random peripheral rotors,

\[
\mathbb E\tau=\frac{11}{2}k-21+21(3/4)^k,
\qquad
\frac{\tau-\frac{11}{2}k}{\sqrt{3k/4}}\ \Longrightarrow\ N(0,1).
\]

These equations concern the *first entry into periodic recurrence* of the full chip-and-rotor configuration, not first return of the chip to the hub.

## Assumptions and scope

Regard every undirected edge as two oppositely directed arcs. The hub rotor visits its outgoing neighbors cyclically in the order

\[
(a_0,b_0,a_1,b_1,\ldots,a_{k-1},b_{k-1}).
\]

It initially points to \(b_{k-1}\), so the first hub departure is to \(a_0\). At each \(a_j\), rotor position \(0\) points to \(h\) and position \(1\) to \(b_j\). At each \(b_j\), position \(0\) points to \(a_j\) and position \(1\) to \(h\); both local orders advance cyclically. Each move advances the rotor at the current chip vertex by one cyclic position and moves the chip along the new rotor. Initially the chip is at \(h\). Exactly the \(2k\) peripheral rotor positions are variable, giving \(4^k\) labelled initial configurations.

A full state comprises the chip's location and every current rotor position. Define \(\tau(\rho)\) to be the least nonnegative integer \(t\) at which that state is recurrent, meaning it belongs to a temporal cycle of the deterministic full-state update. The recurrent-state/unicycle characterization in Holroyd et al. (2008, Theorem 3.8) applies because the bidirected graph is strongly connected: recurrence holds exactly when the rotor arrows form one directed cycle containing the chip.

Call petal \(j\) *bad* precisely if its peripheral rotor bits are \((1,0)\), so its two vertices form \(a_j\to b_j\to a_j\). All three other bit pairs are *good*. For \(J\) the maximum bad index, write \(B=\#\{i<J:i\text{ is bad}\}\).

## Proof

**Step 1: Identify all initial peripheral rotor cycles.** The only directed rotor cycle disjoint from the hub in one petal is the two-cycle \(a_j\leftrightarrow b_j\), arising for bits \((1,0)\). All other peripheral rotor arrows reach the hub. Hence, if every petal is good, the functional rotor graph has exactly the cycle containing the hub, and the chip starts on that cycle. Thus \(\tau=0\).

**Step 2: Check the local two-departure excursion table.** Beginning with the chip at \(h\), make the hub departures \(h\to a_j\) and \(h\to b_j\) consecutively, with no intervening hub departure to another petal. Until the chip returns to \(h\) after the second departure, it cannot affect any other petal. Directly advancing its two peripheral rotors gives the following table, where the counts include both departure moves from the hub:

| Initial bits at \((a_j,b_j)\) | First excursion | Second excursion | Total moves | Final bits |
|---|---:|---:|---:|---|
| \((0,0)\) | 3 | 3 | 6 | \((0,0)\) |
| \((0,1)\) | 4 | 2 | 6 | \((0,1)\) |
| \((1,1)\) | 2 | 4 | 6 | \((1,1)\) |
| \((1,0)\) | 2 | 2 | 4 | \((0,1)\) |

For a good petal, both excursions restore its original good bits. For a bad petal, the two excursions repair the bad internal two-cycle, leaving the good state \((0,1)\).

**Step 3: Locate first recurrence.** If at least one petal is bad, let \(J\) be the largest bad index. The hub scans petals from index zero to \(J-1\), in the two-departure manner above. The duration of these completed scans is \(6(J-B)+4B=6J-2B\). During every state strictly before the subsequent arrival at \(a_J\), the untouched \(a_J\leftrightarrow b_J\) rotor cycle is disjoint from the chip, so the state is not a unicycle and is not recurrent. At the next move the chip moves \(h\to a_J\). All prior bad cycles have been repaired, every later petal is good, and the unique directed rotor cycle is still \(a_J\leftrightarrow b_J\); now the chip is on it. By the unicycle criterion, the resulting state is recurrent. Hence

\[
\tau=6J-2B+1.
\]

**Step 4: Enumerate.** For \(J=j\), the last bad petal has one rotor assignment, all \(k-j-1\) later petals must be good (three choices each), and each preceding petal has three good choices of weight \(z^6\) or one bad choice of weight \(z^4\). The arrival at the last bad petal contributes \(z\). Summing, and adding the \(3^k\) all-good configurations of time zero, gives

\[
H_k(z)=3^k+\sum_{j=0}^{k-1}3^{k-1-j}z(3z^6+z^4)^j.
\]

The greatest exponent is \(6(k-1)+1=6k-5\), reached only when the last petal is bad and every preceding petal is good. There are \(3^{k-1}\) such configurations. Setting \(z=1\) gives exactly \(4^k\) configurations, as required.

**Step 5: Mean and Gaussian limit.** Under the product-uniform initial measure, bad indicators are independent Bernoulli variables with probability \(1/4\). Differentiating the displayed polynomial at \(z=1\), or summing a finite geometric series, yields

\[
\mathbb E\tau=\frac{11}{2}k-21+21(3/4)^k.
\]

Let \(S_k\) denote the total number of bad petals, so \(S_k\sim\mathrm{Binomial}(k,1/4)\). On the event \(S_k>0\), let \(R=k-1-J\) be the number of trailing good petals; it satisfies \(\Pr(R\ge r)=(3/4)^r\) for \(0\le r<k\), hence \(R=O_{\Pr}(1)\). There are \(S_k-1\) earlier bad petals, so the exact entry formula becomes

\[
\tau=6(k-1-R)-2(S_k-1)+1=6k-3-6R-2S_k.
\]

Since \(\Pr(S_k=0)=(3/4)^k\to0\), the binomial central limit theorem, together with the tight trailing correction, proves

\[
\frac{\tau-\frac{11}{2}k}{\sqrt{3k/4}}\Longrightarrow N(0,1).
\]

## Verification

The accompanying standalone Python program `verify_rotor.py` independently implements (i) the formula for \(\tau\), (ii) the rotor-cycle unicycle test at every step, and (iii) complete-state repeat detection, with separate dynamic-state computations. For every \(k=1,\ldots,7\), it exhaustively enumerates all \(4^k\) peripheral initial assignments. All three entry-time algorithms agree, and the empirical histogram equals every coefficient of \(H_k\). There are \(21{,}844\) checked labelled initial states across the seven graph sizes, with observed maximum and maximizing counts agreeing with \(6k-5\) and \(3^{k-1}\). The script requires only the Python standard library and can be run as `python3 verify_rotor.py 7`; `verify_output.txt` records its run.

These finite tests are corroboration; the all-parameter statements are established by the explicit excursion and enumeration proof above, and the central limit theorem is proved by reduction to a binomial count.

## Relationship to prior work

Holroyd, Levine, Mészáros, Peres, Propp and Wilson, *Chip-Firing and Rotor-Routing on Directed Graphs* (public arXiv date 2008-01-22), prove the unicycle criterion for recurrent single-chip states (Theorem 3.8) and Eulerian tours of unicycles (Lemma 4.9). The present theorem applies that criterion to the *first recurrence time from arbitrary peripheral initial rotor assignments* under a prescribed hub scan, and gives an exact labelled distribution, a last-defect structural rule, a rare maximal shell and a Gaussian typical clock. The cited general theorems do not give the petal-specific distribution directly. Poghosyan and Priezzhev's work on Euler tours and unicycles (2013) concerns Eulerian motion of recurrent unicycles and dimer/contour statistics, rather than this initial-transient law. A targeted search found no identical formula, but these searches cannot establish absolute historical priority.

## Limitations

The hub's initial rotor direction, hub ordering, peripheral cyclic orderings and chip start are fixed. Randomness is in the peripheral initial rotors only; the dynamics itself is deterministic. The theorem does not claim a maximum over all hub-rotor initial conditions, other update conventions, other bouquet graphs, or other chip starting sites. The Gaussian limit is asymptotic as the number of triangles grows. Independent formal or expert validation has not been performed, and historical priority in unindexed literature remains uncertain.

## References

1. A. E. Holroyd, L. Levine, K. Mészáros, Y. Peres, J. Propp and D. B. Wilson. *Chip-Firing and Rotor-Routing on Directed Graphs*. arXiv:0801.3306, first posted 2008-01-22. https://arxiv.org/abs/0801.3306. Especially Theorem 3.8 and Lemma 4.9.
2. V. S. Poghosyan and V. B. Priezzhev. *Euler tours and unicycles in the rotor-router model*. arXiv:1310.1225, first posted 2013-10-04. https://arxiv.org/abs/1310.1225.
3. I. Landau and L. Levine. *The Rotor-Router Model on Regular Trees*. arXiv:0705.1562, first posted 2007-05-10. https://arxiv.org/abs/0705.1562.
