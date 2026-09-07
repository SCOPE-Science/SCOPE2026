# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents a former public SCOPE result that failed an independent
> live-literature originality revalidation. The proposed claim is not a validated
> SCOPE finding and must not be cited as one.

## Former record

- **Original record:** `SCOPE-20260907-010`
- **Failed-attempt record:** `SCOPE-FAIL-20260907-031`
- **Title:** Exact Sprague-Grundy periodicity for octal heap game 0.057 (period 148 from preperiod 259)
- **Domain:** Combinatorial Game Theory
- **Original round:** 2026-09-07-first-light-01
- **Original lane:** 26
- **Revalidated at:** 2026-09-07T14:15:25Z

## Claim reviewed

Octal heap game 0.057 (d1=0,d2=5=101,d3=7=111,m=3; G(n)=mex S(n) as defined) is ultimately periodic with minimal preperiod N0=259 and minimal period p=148, i.e. G(n+148)=G(n) for all n>=259; periodic tail values are {1,2,4,7,8} with stated census, global max 8, values to 20000 in {0,1,2,3,4,6,7,8} (5 absent), P-positions exactly {0,1}, and prefix G(0..40)=0,0,1,1,1,2,2,2,3,1,1,1,4,4,4,3,2,2,2,1,1,1,4,2,2,2,6,4,4,4,1,1,1,2,2,2,7,1,1,1,4 proved by 8000-table plus Guy-Smith induction with threshold T*=817.

## Decisive originality failure

Claim-level comparison leaves no room for novelty. (1) Identity: comp_octal.txt explicitly reduces candidate's code 0.057 to standard form 0.055; candidate's own rules (d1=0,d2=5,d3=7) and computed prefix 0,0,1,1,1,2,2,2,3,1,1,1,4,4,4,3,2,2,2,1,1,1,4,2,2,2,6,... match Flammenkamp's .055 prefix 001112223111444322211142226444... through n=26 including the diagnostic 6, and Flammenkamp's easy files list 0.055 with max>=8. (2) Exact constants: Flammenkamp octal.html nontrivial table gives for .055 period 148 preperiod 259 except 2, max G 8, lost 2, ultimate 1, depth 20; solved-structure table gives period 148 preperiod 259 miss 129 solved 1976. These are exactly candidate's minimal pair (259,148), max 8, P-positions {0,1} (lost 2 ultimate 1 means last zero at n=1), and tail set {1,2,4,7,8}. (3) Proof scope: candidate's Guy-Smith lemma with T*=817 is the classical finite-window propagation argument from Guy-Smith 1956, acknowledged as classical in the record itself. The record's assertion that 0.057 was 'previously only tabulated as computed-but-unproved' is contradicted by the database's 'solved 1976' label for the identical game. A fresh computation plus standard induction re-proving an already-recorded minimal period/preperiod is a re-derivation, not an original result, even if the certificate code is new. Hence prior art substantively covers and implies the candidate.

## Nearest prior work found live

- [Sprague-Grundy Values of Octal-Games — Nontrivial Octal-Games table and Nontrivial with known Structure table (.055 entry)](http://wwwhomes.uni-bielefeld.de/achim/octal.html) — covers the claim. Authoritative survey database lists .055 with sgv-prefix 0011122231114443..., type 0, rare 6 last 43, max G 8 index 51, lost 2 ultimate 1, period length 148 preperiod 259 except 2, and in solved-structure table period 148 preperiod 259 miss 129 density 0.4980 solved 1976. Candidate's 0.057 prefix, max 8, lost 2 (P={0,1}), and exact pair (259,148) are identical.
- [A compendium containing all 2*8^3=1024 at most 3 place octal games to find or match its standard form](http://wwwhomes.uni-bielefeld.de/achim/comp_octal.txt) — covers the claim. Row 0.05d maps d=7 (i.e. 0.057) to standard form 0.055 and d=6 (0.056) to 0.054. Hence candidate's 0.057 is by the field's own equivalence the same game as the solved .055 entry above; naming difference does not create novelty.
- [Listing of all the 167 standard forms (easy_octal.txt) and listing sorted by sgv-sequences (easy_sgv.txt)](http://wwwhomes.uni-bielefeld.de/achim/easy_octal.txt) — covers the claim. easy_octal.txt lists 0.57 (two-place game) as p=4 trivial, distinct from 0.055 max>=8 prefix 0011122231114443222111422264441112227111; easy_sgv.txt same. Candidate's computed G(0..40) matches the 0.055 prefix character-for-character through the 6 at n=26, confirming the computed object is the already-tabled .055 sequence, not a newly tabulated sequence.
- [The G-values of various games — Guy and Smith (Proc. Cambridge Philos. Soc. 52, 1956)](https://doi.org/10.1017/S0305004100031509) — related context. Classical octal periodicity (Guy-Smith) theorem whose argument candidate's Lemma 1 re-proves with explicit threshold T*=2N0+2p+m. Provides method, not the specific (259,148) constants; shows candidate's induction method is classical.
- [A note on periodicity in some octal games — Gangolli and Plambeck (Int. J. Game Theory 18, 1989)](https://doi.org/10.1007/BF01254294) — related context. Peer-reviewed octal-periodicity paper building on Guy-Smith, Austin (1976), Kenyon (1967) theses and Winning Ways; exemplifies that finite-window plus propagation proofs for specific octal codes were already a published method and that several codes were proved periodic in that literature. Does not itself claim (259,148) for .055 but contextualizes the 1976 solved date reported by Flammenkamp.
- [Winning Ways for Your Mathematical Plays, Vol.1, Chap.4 Taking and Breaking — Berlekamp, Conway, Guy](https://doi.org/10.1201/9780429487330-4) — related context. Background octal-games chapter defining octal codes, mex, standard-form equivalences (e.g. 0.6 is 0.37, 0.007 is 0.04) of the same kind that makes 0.057 equivalent to 0.055; tables solved vs unsolved octal games. Method and equivalence framework are prior art.

## Recovery conditions

State a materially different claim not covered or implied by the identified prior work, document the distinction with live sources, and submit it to a new independent correctness, originality, and value audit.

## Priority caveat

This FAIL is a literature-coverage finding from the documented live search only; it is not an award of academic priority to any prior author and does not certify correctness or completeness of the prior proofs.

The former result and its artifacts are preserved in this directory solely so that
future SCOPE topic selection can avoid repeating the same claim or can formulate a
genuinely distinct, explicitly sourced claim.
