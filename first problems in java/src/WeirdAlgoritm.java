import java.util.*;

public class WeirdAlgoritm {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long a = input.nextInt();
        System.out.print(a);
        System.out.print(" ");
        while(a != 1){
            if(a % 2 == 0){
                a = a / 2;
            }else {
                a = a * 3 + 1;
            }
            System.out.print(a);
            System.out.print(" ");
        }
    }
}
