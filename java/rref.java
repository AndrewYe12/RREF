import java.io.*;
import java.util.*;
class Matrix{
    private double[][] matrix;

    public Matrix(double[][] matrix){
        this.matrix = matrix;
    }

    public double[][] returnMatrix() {
        return matrix;
    }

    public void changeMatrix(double[][] matrix){
        this.matrix = matrix;
    }

    public static double[][] copyMatrix(double[][] matrix){
        double[][] newMatrix = new double[matrix.length][matrix[0].length];
        for (int i=0; i < matrix.length; i++){
            for (int y=0; y< matrix[0].length; y++){
                newMatrix[i][y] = matrix[i][y];
            }
        }
        return newMatrix;
    }


    protected double[][] rref(){
        int rows = matrix.length;
        int columns = matrix[0].length;
        double[][] rref_form = new double[rows][columns];
        rref_form = Matrix.copyMatrix(matrix);

        for (int i = 0; i < rows; i++){
            boolean foundPivot = false;
            double pivot = 0;
            int count = 0;
            for (int k = 0; k<columns; k++){
                pivot = rref_form[i][k];
                if (pivot != 0){
                    foundPivot = true;
                    break;
                }
                count +=1;
            }
            if (!foundPivot){
                continue;
            }
            for (int k = 0; k < columns; k++) {
                rref_form[i][k] = rref_form[i][k]/pivot;
            }

            for (int k = 0; k<rows; k++){
                if (k == i) {
                    continue;
                }
                double eliminate = rref_form[k][count];
                double[] temp = new double[columns];
                for (int j = 0; j<columns; j++){
                    temp[j] = -eliminate * rref_form[i][j] + rref_form[k][j];
                }
                rref_form[k] = temp;
            }
        }

           
        double[] example = new double[columns];
        for (int i = Math.min(rows, columns)-1; i>-1; i--){
            if (rref_form[i] == example){
                for (int k = i; i<rows-1; i++){
                    rref_form[i] = rref_form[i+1];
                    rref_form[rows-1] = example;
                }
                
            }
        }
        
        int minOfMatrix = Math.min(rows, columns);
        int[] sortThisArray = new int[minOfMatrix];
        for (int i = minOfMatrix-1; i > -1; i--){
            int k;
            for (k = 0; k <columns; k++){
                double pivot = rref_form[i][k];
                if (pivot !=0){
                    break;
                }
            }
            sortThisArray[i] = k;
        }
        
        double[][] newMatrix = new double[rows][columns];
        int[] constantArray = Arrays.copyOf(sortThisArray, sortThisArray.length);
        Arrays.sort(sortThisArray);
        for (int i = 0; i <sortThisArray.length; i++){
            int temp = constantArray[i];
            int index;
            for (index = 0; index<sortThisArray.length; index++){
                if (sortThisArray[index] == temp){
                    break;
                }
            }
            newMatrix[index] = rref_form[i];
        }

        return newMatrix;
    }    

    public static void main(String args[]){
        double[][] yay = {{0,0,1,0,0,0,0},{1,0,0,0,0,0,0},{0,0,0,1,0,0,0},{0,0,0,0,0,0,0,},{0,0,0,0,0,0,1},{0,0,0,1,0,0,0}};
        Matrix p = new Matrix(yay);
        System.out.print(Arrays.deepToString(p.rref()));
    }
}

