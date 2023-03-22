//conditions 
// selling price > buying price
// profit must be highest , from right to left 


// TWO FOR STATEMENRENRS???? 
// TODO: stop acc being dumb 

//maybes sliding window 
int maxProfit(int* prices, int pricesSize){
    int profit = 0;
    for (int i = 0; i < pricesSize; i++){
        for (int j = i+1 ; j< pricesSize; j++ ){
            if (prices[j] > prices[i]){
                if ((prices[j] - prices[i]) > profit){
                    profit = (prices[j] - prices[i]);
                }
            }
        }
    }
        return profit;
    }
    