#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

// Exhaustively list universal five-symbol words, modulo letter relabeling.
// For each target permutation, state p is the length of its greedy match.
// Cutoffs follow from the minimum complete lengths for smaller alphabets.
namespace {
constexpr int Q = 5, NP = 120;
const int minimum[6] = {0,1,3,7,12,19};
std::array<std::array<unsigned char,Q>,NP> permutations;
std::array<unsigned char,NP> progress{};
std::string word;
std::vector<std::string> complete_words;
int final_length;

bool admissible_prefix(int depth) {
    for(int t=1;t<=Q;t++) {
        if(depth < final_length - minimum[Q-t]) continue;
        for(int i=0;i<NP;i++) if(progress[i]<t) return false;
    }
    return true;
}
void visit(int known) {
    if(static_cast<int>(word.size())==final_length) {
        complete_words.push_back(word);
        return;
    }
    for(int x=0;x<=known && x<Q;x++) {
        if(!word.empty() && word.back()==static_cast<char>('0'+x)) continue;
        auto saved=progress;
        for(int i=0;i<NP;i++) if(progress[i]<Q && permutations[i][progress[i]]==x) ++progress[i];
        word.push_back(static_cast<char>('0'+x));
        if(admissible_prefix(static_cast<int>(word.size()))) visit(known+(x==known));
        word.pop_back();
        progress=saved;
    }
}
} // namespace

int main(int argc,char **argv) {
    final_length=(argc>1)?std::stoi(argv[1]):19;
    if(final_length!=18 && final_length!=19) return 2;
    std::array<unsigned char,Q> a{0,1,2,3,4};
    int i=0;
    do{permutations[i++]=a;}while(std::next_permutation(a.begin(),a.end()));
    visit(0);
    std::sort(complete_words.begin(),complete_words.end());
    for(const auto &s:complete_words)std::cout<<s<<'\n';
    std::cerr<<"length="<<final_length<<" canonical="<<complete_words.size()<<'\n';
}
