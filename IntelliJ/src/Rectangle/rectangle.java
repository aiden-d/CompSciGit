package Rectangle;

public class rectangle  {
    int xPos =0;
    int yPos =0;
    float width =3;
    float height = 3;
    public static void main(String[] args) {

    }
    public rectangle(){}

    public rectangle(int xPos,int yPos){
        this.xPos = xPos;
        this.yPos = yPos;
    }

    public rectangle(float width,float height){
        this.width = width;
        this.height = height;
    }
    public rectangle(float width,float height,int xPos,int yPos) {
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
            int ii =0;
            while (ii<width){

                if((xPos+ii==xPos||xPos+ii+1==xPos+width)&&(yPos+i==yPos||yPos+i==yPos+height-1)){str = str + " *";}
                str = str+"  ";
                ii++;
            }
            i++;
            System.out.println(str);


        }
    }


}