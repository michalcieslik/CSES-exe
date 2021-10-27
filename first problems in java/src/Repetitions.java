import java.util.*;

public class Repetitions {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String a = input.nextLine();
        int max = 1;
        int current = 1;
        char b;
        if(a.length() > 0)
            b = a.charAt(0);
        else {
            System.out.print(0);
            return;
        }
        for(int i = 1; i < a.length(); i++) {
            if (a.charAt(i) == b){
                current++;
                if(current > max)
                    max = current;
            }else{
                b = a.charAt(i);
                current = 1;
            }
        }
        System.out.print(max);
    }
}
