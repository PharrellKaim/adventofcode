import java.io.File;
import java.io.FileNotFoundException; 
import java.util.Scanner;

public class day1{

    public static void parseData(int[] arr){
        try {
            File myObj = new File("/Users/pharrellkaim/Documents/Dokumente – MacBook Pro von Pharrell/GitHub/adventofcode/2022/day1/inputDay1.txt");
            Scanner freader = new Scanner(myObj);
            int i = 0;
            int sum = 0;
            while(freader.hasNextLine()){
                int data = Integer.parseInt(freader.nextLine());
                sum = sum + data;
                if (data == 0){
                    arr[i] = sum;
                    sum = 0;
                }
            }
            freader.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
    }

    public static void part1(){

    }

    public static void main(String[] args){
        int arr[] = new int[0];
        parseData(arr);
        System.out.println(arr);
    }
}

