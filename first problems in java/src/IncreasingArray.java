import java.util.*;

public class IncreasingArray {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < n; i++){
            int b = input.nextInt();
            list.add(b);
        }
        long moves = 0;
        int previous = -1;
        int that = -1;
        for(int i = 0; i < n; i++){
            that = list.get(i);
            if(that < previous){
                moves = moves + (previous - that);
                list.set(i, previous);
                that = previous;
            }
            previous = that;
        }
        System.out.print(moves);
    }
}
