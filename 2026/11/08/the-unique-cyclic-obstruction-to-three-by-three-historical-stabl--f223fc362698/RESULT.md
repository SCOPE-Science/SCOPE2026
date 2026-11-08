# The unique cyclic obstruction to three-by-three historical stable-matching completeness

## Finding

In a complete strict three-by-three marriage market, a stable matching is *terminal-history reachable* if some finite sequence of single-agent arrivals and departures, starting with nobody active and using only the six eventual agents, produces it by stable proposal-chain continuation after every change. Repeated departures and re-entries are allowed, and a target matching is allowed to dictate the history.

**Exact classification.** Among all \(6^6=46{,}656\) labeled preference profiles, exactly **12** admit any stable matching that is not terminal-history reachable. These 12 profiles are exactly the orbit, under independent relabelings of the two sides, of the cyclic market
\[
\begin{array}{lll}
m_1:w_1\succ w_2\succ w_3,&m_2:w_2\succ w_3\succ w_1,&m_3:w_3\succ w_1\succ w_2,\\
w_1:m_2\succ m_3\succ m_1,&w_2:m_3\succ m_1\succ m_2,&w_3:m_1\succ m_2\succ m_3.
\end{array}
\]
Each bad profile has exactly three stable matchings, of which exactly one (the cyclic middle matching) is unreachable. Every stable matching of each of the other \(46{,}644\) profiles is reachable. Under six independent impartial-culture rankings, the probability of incomplete historical reachability is therefore exactly
\[
\frac{12}{46{,}656}=\frac1{3888}.
\]
The complete joint classification by the number of stable matchings and the number reachable is

| Stable | Reachable | Number of profiles |
|---:|---:|---:|
| 1 | 1 | 34,080 |
| 2 | 2 | 11,484 |
| 3 | 2 | 12 |
| 3 | 3 | 1,080 |

## Assumptions and scope

There are three labeled men and three labeled women; each strictly ranks all three members of the other side above remaining unmatched. Preferences are fixed even across exits and re-entries. A stable matching has no blocking pair. Every event adds or removes one agent, and any resulting unmatched proposer initiates the standard best-acceptable-partner proposal chain, displacing an incumbent when preferred by the recipient. Only stable outcomes between events are admissible. A history uses no temporary agents outside the terminal six. This is a finite classification of these markets, not a general assertion for larger markets or incomplete acceptability.

## Proof

**1. Every five-agent stable predecessor can be reached from the empty market.** After deleting one agent, the smaller side has two agents. Complete acceptability forces every member of that side to be matched in any stable matching. By the rural-hospitals property, the unmatched member of the larger side is the same in all stable matchings. Thus there are at most two stable matchings: once the unmatched person is fixed, the two matched partners can only be kept or swapped. If there are two, they are the two opposite-side-optimal stable matchings. To produce either, enter the agents of the opposite side first, then enter all proposing-side agents in any order. The successive proposal-chain continuations are exactly incremental deferred acceptance, and the final matching is the proposer-optimal stable matching. Thus **each stable five-agent matching is accessible by an entry-only history**. The same is trivially true when fewer agents are active.

**2. Codimension-one criterion.** Let \(\mathcal S(M)\) be the stable set of a full profile. For each one of the six possible absent agents \(x\), enumerate every stable matching \(\nu\) of the five-agent submarket \(M-x\). Let \(E_x(\nu)\) be the unique stable outcome obtained when \(x\) enters and runs its proposal chain. Put
\[
R(M)=\bigcup_{x}\{E_x(\nu):\nu\in\mathcal S(M-x)\}.
\]
Every \(\mu\in R(M)\) is terminal-history reachable by Step 1 followed by the final entry. Conversely, in any history reaching the full market with \(\mu\) for the *first* time, the immediately preceding market has exactly five agents and its matching is stable. The last entry therefore produces \(\mu\in R(M)\). If a history first visits the full population in a different matching and later changes it, the *first* visit with the target still must be preceded by an entry from five agents (unless a preceding full-state visit already had the target). Consequently \(R(M)\) is exactly the historically reachable subset despite arbitrarily many exits and re-entries.

**3. Exhaustive finite classification.** The attached independently implemented Python and C++ checkers evaluate the finite criterion, with no random samples. They enumerate each of the \(6^6\) combinations of strict rankings of three partners; enumerate the six perfect matchings of the full market and the six possible two-pair matchings of each five-agent submarket; reject an assignment if an active unmatched pair blocks it; perform each proposal chain from every stable five-agent matching; and compare the resulting set \(R(M)\) with \(\mathcal S(M)\). Both programs output the table in the Finding section. The Python implementation additionally generates all images of the displayed cyclic profile under the \(3!\times3!\) independent relabeling group and verifies that **the set of all deficient profiles equals that orbit**. The orbit contains 12 distinct profiles (the cyclic simultaneous rotation has stabilizer of size three, so \(36/3=12\)). This establishes the global upper bound, while the known cyclic market establishes its nonzero obstruction.

All loops are bounded explicitly by three agents, three partners, six choices per ranked list and finitely many possible matchings. Checking all \(6^6\) profiles is exhaustive here; no extrapolation from finite computations to infinite populations is made.

## Verification

Run `python3 reachability_verify.py` in an ordinary Python 3 environment. It independently reconstructs the count table, checks that every computed entrant continuation is stable, checks that every five-agent submarket has one or two stable matchings, and compares the 12 deficient profiles with the relabeling orbit. Run `g++ -O2 -std=c++17 reachability_census.cpp -o reachability_census && ./reachability_census` to obtain the same counts using a second implementation. No third-party packages or external data are needed. The code establishes finite exhaustive claims; the codimension-one equivalence above is an independent mathematical reduction of arbitrary-length histories.

## Relationship to prior work

Yang's 2026 *Stable Matchings and Their Histories* supplies the cyclic three-by-three nonreachability example and defines the relevant history model, but not the universal classification or the exact impartial-culture incidence. The cyclic example alone supplies a lower bound of 12 labeled failures, because its independent relabeling orbit has size 12; the new result proves this is the **entire** failure set. Cheng's 2016 random-order-reachability work concerns broader complexity and entry-only histories; those statements do not determine this finite orbit classification. Prior published three-by-three stability censuses record \(34{,}080\), \(11{,}484\), and \(1{,}092\) profiles with one, two, and three stable matchings respectively; such marginal counts do not determine which middle stable matchings are history-reachable. In fact, the present classification shows that 1,080 of the 1,092 three-stable profiles have all three matchings reachable.

## Limitations

The exact distribution assumes complete, uniformly random strict preferences, not correlated or incomplete rankings. It counts profiles for which *some* stable matching is unreachable, not the probability that an arbitrary policy or random history selects that matching. The proof relies on exhaustive finite computation for the complete orbit exclusion and should not be read as an infinite-size structural theorem. The checker is transparent and independently reproduced but is not a formal proof-assistant certificate. Unindexed mathematical equivalents may exist; independent research review has not been performed.

## References

1. Yi-You Yang, *Stable Matchings and Their Histories: Historical Reachability under Population Shocks*, arXiv:2609.20176 (2026), Sections 2–4, https://arxiv.org/html/2609.20176.
2. Christine T. Cheng, *On the Stable Matchings That Can Be Reached When the Agents Go Marching in One by One*, SIAM Journal on Discrete Mathematics 30 (2016), 2047–2063, https://doi.org/10.1137/140996690.
3. Matvey Borodin et al., *Sequences of the Stable Matching Problem*, arXiv:2201.00645 (first submitted 2021), https://arxiv.org/abs/2201.00645; corresponding stable-count table OEIS A344666, https://oeis.org/A344666.
