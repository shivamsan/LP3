import java.util.*;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class fracknap {
    static int profit;

    public static int Knapsac(int[] p, int[] w, int c) {
        int n = p.length;
        double[] ratio = new double[n];

        for (int i = 0; i < n; i++) {
            ratio[i] = p[i] / w[i];
        }

        // Arrays.sort(ratio, Collections.reverseOrder());

        // Sort in ascending order first
        Arrays.sort(ratio);

        // Reverse the array to get descending order
        for (int i = 0; i < ratio.length / 2; i++) {
            double temp = ratio[i];
            ratio[i] = ratio[ratio.length - 1 - i];
            ratio[ratio.length - 1 - i] = temp;
        }

        for (int i = 0; i < n; i++) {
            if (c > 0 && w[i] <= c) {
                c = c - w[i];
                profit = profit + p[i];

            } else
                break;

            if (c > 0) {
                profit = profit + p[i] * (c / w[i]);
            }
        }

        return profit;

    }

    public static void main(String[] args) {
        int[] profit = { 25, 24, 15 };
        int[] weight = { 18, 15, 10 };
        int capacity = 20;

        System.out.println(Knapsac(profit, weight, capacity));

    }
}