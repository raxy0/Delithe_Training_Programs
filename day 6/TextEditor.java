import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TextEditor {

    public static void main(String[] args) {
      
        Scanner sc = new Scanner(System.in);
        String str = "";
        int top = 0;
        int q = Integer.parseInt(sc.nextLine());
        MyStack stack = new MyStack(q);
        for(int i = 0; i < q; ++i){
            String st[] = sc.nextLine().split(" ");
            int query = Integer.parseInt(st[0]);
            if(query == 1){
                Node newNode = new Node(query,str.length());
                stack.top++;
                stack.list[stack.top] = newNode;
                str += st[1];
            } else if(query == 2){
                int k = Integer.parseInt(st[1]);
                Node newNode = new Node(query,str.substring(str.length()-k));
                stack.top++;
                stack.list[stack.top] = newNode;
                str = str.substring(0,str.length()-k);
            } else if(query == 3){
                int index = Integer.parseInt(st[1]);
                System.out.println(str.charAt(index-1));
            } else if(query == 4){
                Node newNode = stack.list[stack.top];
                stack.top--;
                if(newNode.qtype == 1){
                    str = str.substring(0,newNode.idx);
                } else if(newNode.qtype == 2){
                    str += newNode.w;
                }
            }
        }
    }
}
class MyStack{
    Node list[];
    int top;
    MyStack(int size){
        this.list = new Node[size];
        this.top = -1;
    }
}
class Node{
    int qtype;
    int idx;
    String w;
    Node(int x, String y){
        this.qtype = x;
        this.w = y;
    }
    Node(int x, int index){
        this.qtype = x;
        this.idx = index;
    }
}