import java.util.*;

public class MissingNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        ArrayList<Integer> lista = new ArrayList<Integer>();
        for(int i = 1; i < a; i++){
            int b = input.nextInt();
            lista.add(b);
        }
        Collections.sort(lista);
        for(int i = 0; i < a - 1; i++){
            if(lista.get(i) != i + 1){
                System.out.print(i + 1);
                return;
            }
        }
        System.out.print(a);
    }
}
