package java;

/**
 * Rectangle
 */
public class Rectangle  {
    int xPos;
    int yPos;
    float width;
    float height;
    public static void main(String[] args) {
        
    }
    public Rectangle(){}

    public Rectangle(int xPos,int yPos){
        this.xPos = xPos;
        this.yPos = yPos;
    }

    public Rectangle(float width,float height){
        this.width = width;
        this.height = height;
    }
    public Rectangle(float width,float height,int xPos,int yPos) {
        this.width = width;
        this.height = height;
        this.xPos = xPos;
        this.yPos = yPos;
    }
    public int[] getPosition (){
        int [] position = {xPos, yPos};
        return position;
    }

    public int getxPos(){return xPos;}
    public int getyPos(){return yPos;}
    public float getWidth(){return width;}
    public float getheight(){return height;}
    public float getArea(){return width*height;}
    public String toString(){return "Rectangle (" +xPos+","+yPos+")-("+(xPos+width)+","+yPos+height+")";}

    public void printShape() {
       int i = 0;
        while(i<height){
            String str = "";
            while (i<width){
                str = str + "*";
            }
            System.out.println(str);

       } 
    }

    
}