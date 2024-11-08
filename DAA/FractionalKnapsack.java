import java.util.Arrays;
import java.util.Comparator;

public class FractionalKnapsack {

    public static double fractionalKnapsack(int[] p, int[] w, int c) {
        int n = p.length;
        double profit = 0.0;

        // Create an array of items with profits, weights, and profit-to-weight ratios
        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            items[i] = new Item(p[i], w[i], (double) p[i] / w[i]);
        }

        // Sort items by ratio in descending order
        Arrays.sort(items, Comparator.comparingDouble(Item::getRatio).reversed());

        for (Item item : items) {
            if (c > 0 && item.weight <= c) {
                // Take the whole item
                c -= item.weight;
                profit += item.profit;
            } else {
                // Take a fraction of the item
                profit += item.profit * ((double) c / item.weight);
                break;
            }
        }

        return profit;
    }

    public static void main(String[] args) {
        int[] profit = { 25, 24, 15 };
        int[] weight = { 18, 15, 10 };
        int capacity = 20;

        System.out.println("Maximum profit: " + fractionalKnapsack(profit, weight, capacity));
    }
}

// Helper class to store profit, weight, and ratio of each item
class Item {
    int profit;
    int weight;
    double ratio;

    public Item(int profit, int weight, double ratio) {
        this.profit = profit;
        this.weight = weight;
        this.ratio = ratio;
    }

    public double getRatio() {
        return ratio;
    }
}
