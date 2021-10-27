import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.*;

public class Permutations{
    public static void main(String[] args) throws IOException {
        InputStreamReader inputStreamReader = new InputStreamReader(System.in);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

        int a = Integer.parseInt(bufferedReader.readLine());
        if(a == 1) {
            System.out.print(1);
            return;
        }
        if(a < 4 && a > 1)
            out.print("NO SOLUTION");
        else {
            for(int i = 2; i <= a; i = i + 2){
                out.print(i + " ");
            }
            for(int i = 1; i <= a; i = i + 2){
                out.print(i + " ");
            }
        }
        out.flus
    }
}
