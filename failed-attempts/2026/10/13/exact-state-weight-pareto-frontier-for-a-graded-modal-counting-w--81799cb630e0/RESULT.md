# Exact state--weight Pareto frontier for a graded-modal counting witness

## Finding

For every integer \(N\ge 1\), consider the graded-modal formula

\[
\chi_N:=p\wedge\Box\neg p\wedge\Diamond^N\top\wedge\neg\Diamond^{N+1}\top.
\]

In the weighted \(B^\infty\)-semantics of Bellas Acosta and Venema, fix the number \(m\ge2\) of states. Among all finite \(m\)-state models satisfying \(\chi_N\) at the distinguished state, the exact minimum possible model weight is

\[
\boxed{\;w_{\min}(N,m)=\left\lceil\frac{N}{m-1}\right\rceil.\;}
\]

Consequently, the smallest weighted model has exactly two states and weight \(N\), while the smallest ordinary Kripke model has exactly \(N+1\) states. The family therefore gives an exact Pareto frontier: successor multiplicity can be compressed into fewer states precisely by increasing the largest finite transition weight.

## Assumptions and scope

The notation and semantics are those of *Counting to Infinity: Graded Modal Logic with an Infinity Diamond*. A finite \(B^\infty\)-model has transition weights in \(\mathbb N\cup\{\infty\}\). At a state \(s\),

\[
s\Vdash\Diamond^k\varphi
\quad\Longleftrightarrow\quad
\sum_{t\Vdash\varphi}\sigma_s(t)\ge k.
\]

Its weight \(w(\mathbb S)\) is the largest finite value taken by any transition-weight function. Ordinary Kripke models embed as the special case in which all transition weights are \(0\) or \(1\).

The formula \(\chi_N\) uses only ordinary graded modalities; the infinity diamond is not needed for the witness. The claim concerns finite models and exact cardinality \(m\) of the carrier.

## Proof

Let \((\mathbb S,s)\) be a finite weighted model satisfying \(\chi_N\). The conjunct

\[
\Diamond^N\top\wedge\neg\Diamond^{N+1}\top
\]

says exactly that the total outgoing weight from \(s\) is \(N\). In particular no outgoing weight is \(\infty\).

The conjunct \(p\wedge\Box\neg p\) says that \(s\) itself satisfies \(p\), while every positive-weight successor of \(s\) satisfies \(\neg p\). Hence \(\sigma_s(s)=0\). In an \(m\)-state model there are therefore at most \(m-1\) states on which the total weight \(N\) can be placed.

If all finite transition weights were at most \(q\), then

\[
N\le (m-1)q.
\]

Thus every such model satisfies

\[
w(\mathbb S)\ge \left\lceil\frac{N}{m-1}\right\rceil.
\]

For the matching upper bound, distribute \(N\) as evenly as possible among the \(m-1\) non-root states: write

\[
N=(m-1)a+r,\qquad 0\le r<m-1,
\]

and assign weight \(a+1\) to \(r\) of them and weight \(a\) to the rest, omitting zero-weight states when \(a=0\). Give \(p\) only to the root and set all other transition weights to zero. Then \(\chi_N\) holds and the largest weight is

\[
a+\mathbf 1_{r>0}=\left\lceil\frac{N}{m-1}\right\rceil.
\]

This proves the exact frontier.

Taking \(m=2\) gives the smallest possible weighted carrier, with one non-root state carrying weight \(N\). For an ordinary Kripke model every weight is \(0\) or \(1\). Hence \(N\) units of outgoing weight require \(N\) distinct non-root successors, so at least \(N+1\) states are necessary; a root together with exactly \(N\) terminal successors attains the bound.

## Verification

The bundled verifier performs two independent checks. First, it exhaustively enumerates weak compositions of \(N\) into \(m-1\) transition weights for a grid of small \((N,m)\), and confirms that the least possible maximum part is exactly \(\lceil N/(m-1)\rceil\). Second, it constructs the balanced extremal distribution for a much larger grid and checks both the graded-modal truth conditions and the Kripke \(0/1\)-weight threshold.

The verifier returns `VERIFY_OK 199425 exact assertions`.

## Relationship to prior work

Bellas Acosta and Venema define the weighted \(B^\infty\)-semantics, prove that it extends ordinary Kripke semantics, define separate state-size and weight measures, and prove a small-model theorem bounding both quantities. Their paper also remarks that weighted coalgebras can be more compact representations of Kripke structures.

The displayed formula is a quantitative sharpening of that compactness observation. The inspected source does not give an exact state--weight frontier, nor the minimum Kripke size for this witness family. Candidate-specific published-finding corpus searches, exact web searches for graded-modal size/weight tradeoffs, and searches of the cumulative research ledgers found no equivalent statement.

The conclusion is deliberately narrow: it isolates one canonical exact-count family and computes its complete two-parameter resource curve. It does not improve the paper's general small-model theorem for arbitrary formulas.

## Limitations

The proof is elementary once the weighted semantics is available, so the formula may be known informally to specialists as an obvious compression example. The originality claim is only for the exact Pareto-frontier formulation and its systematic comparison with Kripke size. No independent audit has yet been performed.

## References

1. Ignacio Bellas Acosta and Yde Venema, “Counting to Infinity: Graded Modal Logic with an Infinity Diamond,” *The Review of Symbolic Logic* 17(1), 1--35, DOI 10.1017/S1755020322000247. Published online 8 July 2022. Primary MSC 03B45.
2. F. De Caro, “Graded modalities II: Canonical models,” *Studia Logica* 47(1), 1--10 (1988), cited by Bellas Acosta and Venema for the weighted-model perspective.
