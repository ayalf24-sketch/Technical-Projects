echo "# Technical-Projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ayalf24-sketch/Technical-Projects.git
git push -u origin main


import java.io.*;   // reading a file
import java.util.*;

public class Sudoku {    
    private int[][] grid;
    
    private boolean[][] valIsFixed;
    
  
    private boolean[][][] subgridHasVal;
    
    private boolean [][] ValRow;
    private boolean [][] ValCol;
    
    
    public Sudoku() {
        this.grid = new int[9][9];
        this.valIsFixed = new boolean[9][9];     
        
        
        this.subgridHasVal = new boolean[3][3][10];        

        
        this.ValRow = new boolean [9][10];
        this.ValCol = new boolean [9][10];
    }
    
    public void placeVal(int val, int row, int col) {
        this.grid[row][col] = val;
        this.subgridHasVal[row/3][col/3][val] = true;
      
        this.ValRow[row][val] = true;
        this.ValCol[col][val] = true;
    }
        
    
    public void removeVal(int val, int row, int col) {
        this.grid[row][col] = 0;
        this.subgridHasVal[row/3][col/3][val] = false;
        
  
        this.ValRow[row][val] = false;
        this.ValCol[col][val] = false;
    }  
        

    public void readConfig(Scanner input) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int val = input.nextInt();
                this.placeVal(val, r, c);
                if (val != 0) {
                    this.valIsFixed[r][c] = true;
                }
            }
            input.nextLine();
        }
    }
                      
    public void printGrid() {
        for (int r = 0; r < 9; r++) {
            this.printRowSeparator();
            for (int c = 0; c < 9; c++) {
                System.out.print("|");
                if (this.grid[r][c] == 0) {
                    System.out.print("   ");
                } else {
                    System.out.print(" " + this.grid[r][c] + " ");
                }
            }
            System.out.println("|");
        }
        this.printRowSeparator();
    }
        
    private static void printRowSeparator() {
        for (int i = 0; i < 9; i++) {
            System.out.print("----");
        }
        System.out.println("-");
    }
    
    
    public boolean checkifSafe(int row, int col, int val){ // checks if value is already in its row or col or subgrid if not then its safe to place
    
        if(this.subgridHasVal[row/3][col/3][val] == true)
            return false;
        if(this.ValRow[row][val] == true)
            return false;
        if(this.ValCol[col][val] == true)
            return false;
       
        return true;
        
    }
         
    /*
     * This is the key recursive-backtracking method.  Returns true if
     * a solution has already been found, and false otherwise.
     */
    private boolean solveRB(int n) {
                
        if(n == 81)
            return true;
        int row = n /9;
        int col = n % 9;

        if(valIsFixed[row][col])
            return solveRB(n+1);
       for(int i = 1; i <= 9; i++){
       if(checkifSafe(row, col, i) == true){ 
            placeVal(i, row, col);
            if(solveRB(n+1) == true)
                return true;
            else
                removeVal(i, row, col);
       }
    }
        return false;
    } 
    
    /*
     * public "wrapper" method for solveRB().
     * Makes the initial call to solveRB, and returns whatever it returns.
     */
    public boolean solve() { 
        boolean foundSol = this.solveRB(0);
        return foundSol;
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Sudoku puzzle = new Sudoku();
        
        System.out.print("Enter the name of the puzzle file: ");
        String filename = scan.nextLine();
        
        try {
            Scanner input = new Scanner(new File(filename));
            puzzle.readConfig(input);
        } catch (IOException e) {
            System.out.println("error accessing file " + filename);
            System.out.println(e);
            System.exit(1);
        }
        
        System.out.println();
        System.out.println("Here is the initial puzzle: ");
        puzzle.printGrid();
        System.out.println();
        
        if (puzzle.solve()) {
            System.out.println("Here is the solution: ");
        } else {
            System.out.println("No solution could be found.");
            System.out.println("Here is the current state of the puzzle:");
        }
        puzzle.printGrid();  
    }    
}
