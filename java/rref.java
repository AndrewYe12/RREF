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

    public static double[][] createIdentity(int sizeMatrix){
        double[][] newMatrix = new double[sizeMatrix][sizeMatrix];
        for (int i = 0; i<sizeMatrix; i++){
            newMatrix[i][i] = 1;
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
        for (int i = 0; i<Math.min(rows,columns); i++){ //change this to go in reverse order if there is a bug, but i think it works for now.
            if (Arrays.equals(rref_form[i], example)){
                for (int k = i; k<rows-1; k++){
                    rref_form[k] = rref_form[k+1];
                }
                rref_form[rows-1] = example;
            }
        }
        
        int minOfMatrix = Math.min(rows, columns);
        int[] sortThisArray = new int[minOfMatrix];
        for (int i = minOfMatrix-1; i > -1; i--){
            int k;
            double pivot=-1;
            for (k = 0; k <columns; k++){
                pivot = rref_form[i][k];
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

    protected double[][] inverse(){
        int rows = matrix.length;
        int columns = matrix[0].length;
        double[][] rref_form = new double[rows][columns];
        rref_form = Matrix.copyMatrix(matrix);
        
        double[][] inverse = new double[rows][rows];
        inverse = Matrix.createIdentity(rows);

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

            for (int k = 0; k< rows; k++){
                inverse[i][k] = inverse[i][k]/pivot;
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
                
                double[] extraTemp = new double[rows];
                for (int j = 0; j<rows; j++){
                    extraTemp[j] = -eliminate * inverse[i][j] + inverse[k][j];
                }
                inverse[k] = extraTemp;
            }
        }

          
        double[] example = new double[columns];
        for (int i = Math.min(rows, columns)-1; i>-1; i--){
            if (Arrays.equals(rref_form[i], example)){
                double[] newTemp = inverse[i];
                for (int k = i; k<rows-1; k++){
                    rref_form[k] = rref_form[k+1];
                    inverse[k] = inverse[k+1];
                }
                rref_form[rows-1] = example;
                inverse[rows-1] = newTemp;
            }
        }
        
        int minOfMatrix = Math.min(rows, columns);
        int[] sortThisArray = new int[minOfMatrix];
        int countZeroRows = 0;
        for (int i = minOfMatrix-1; i > -1; i--){
            int k;
            double pivot=-1;
            for (k = 0; k <columns; k++){
                pivot = rref_form[i][k];
                if (pivot !=0){
                    break;
                }
            }

            if (pivot == 0){
                sortThisArray[i] = rows-countZeroRows-1;
                countZeroRows += 1;
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

        double[][] newInverse = new double[rows][rows];
        for (int i = 0; i<sortThisArray.length ; i++){
            int temp = constantArray[i];
            int index;
            for (index = 0; index< sortThisArray.length;index++){
                if (sortThisArray[index] == temp){
                    break;
                }
            }
            newInverse[index] = inverse[i];
        }
        double[] newExample = new double[rows];
        for (int i = 0; i< rows; i++){
            if (Arrays.equals(newInverse[i], newExample)){
                newInverse[i] = inverse[i];
            }
        }



        return newInverse;
    }

    public static void main(String args[]){
        double[][] yay = {{0,0,0,3,78,8,0},{2,41,3,98,9,89,9},{6,78,4,2,6,76,7},{32,4,8,6,7,5,9},{6,4,8,3,67,8,878}};
        Matrix p = new Matrix(yay);
        System.out.println(Arrays.deepToString(p.rref()));
        System.out.print(Arrays.deepToString(p.inverse()));
    }
}

