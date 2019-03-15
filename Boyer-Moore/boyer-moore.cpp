#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

std::vector<int> Z_algo(std::string S){
    int n = S.size();
    int r = 0;
    int l = 0;
    std::vector<int> Z(n,0);
    Z[0] = n;
    for(int k = 1; k < n; k++){
        if (k > r) {
            int z_k = 0;
            while (k+z_k < n && S[z_k]==S[k+z_k]) z_k++;
            Z[k] = z_k;
            if (z_k > 0) {
                r = k + z_k - 1;
                l = k;
            }
        }
        else {
            int k2 = k-l;
            if (Z[k2] < r-k+1) Z[k] = Z[k2];
            else {
                int z_k = r-k+1;
                while (k+z_k < n && S[z_k]==S[k+z_k]) z_k++;
                Z[k] = z_k;
                r = k + z_k - 1;
                l = k;
            }
        }
    }
    return Z;
}

std::pair<std::vector<int>,std::vector<int>> precompute_L_and_l(std::string P){
    std::string PR = P;
    std::reverse(std::begin(PR), std::end(PR));
    std::vector<int> N = Z_algo(PR);
    std::reverse(std::begin(N), std::end(N));
    int n = N.size();
    
    std::vector<int> L(n,0);
    std::vector<int> l(n,0);
    for(int j = 0; j < n; j++) {
        int i = n - N[j];
        L[i] = j+1;
        if (N[j]==j+1) l[n-j-1] = j+1;
    }
    for(int i = n-2; i >= 0; i--) l[i] = std::max(l[i+1], l[i]);
    return std::make_pair(L,l);
}

std::map<char,std::vector<int>> extended_bad_rule(std::string P){
    std::map<char,std::vector<int>> R;
    int n = P.size();
    for(int i = 0; i < n; i++){
        if (R.find(P[i]) == R.end()){
            R[P[i]] =  {};
        }
        R[P[i]].push_back(i);
    }
    return R;
}

int good_rule(int i, std::vector<int> &L, std::vector<int> &l){
    int n = L.size();
    if (L[i] > 0) return n - L[i];
    else return n - l[i];
}

int bin_search(int a, int b, int i, std::vector<int> R){
    if (a == b) return R[a];
    int m = (a+b)/2;
    if (R[m+1] < i) return bin_search(m+1, b, i, R);
    else return bin_search(a, m, i, R);
}

int bad_rule(int i, char P_h, std::map<char,std::vector<int>> &R, int n){
    if  (R.find(P_h) == R.end()) return n-i+1;
    if (R[P_h][0] > i) return n-i+1;
    return i - bin_search(0,R[P_h].size()-1,i, R[P_h]) ;
}

std::vector<int> boyer_moore(std::string P, std::string T){
    std::vector<int> res;
    std::vector<int> L,l;
    std::tie(L,l) = precompute_L_and_l(P);
    std::map<char,std::vector<int>> R = extended_bad_rule(P);

    int n = P.size();
    int m = T.size();
    int k = n-1;
    while (k < m) {
        int i = n-1;
        int h = k;
        while ((i >= 0) && (P[i] == T[h])) {
            i--; h--;
        }
        if (i == -1){
            res.push_back(k);
            k = k + n - l[1];
        }
        else{
            k = k + std::max(good_rule(i,L,l),bad_rule(i,T[h],R,n));
        }
    }
    return res;
}

int main(){
    std::string P,T;
    getline(std::cin,P);
    getline(std::cin,T);
    std::vector<int> res = boyer_moore(P,T);
    for(int i = 0; i < res.size(); i++) std::cout << res[i] << " ";
    std::cout << std::endl;
    return 0;
}
