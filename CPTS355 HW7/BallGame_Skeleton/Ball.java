import java.applet.*;
import java.util.Random;
import java.awt.*;
import java.util.*;
import java.net.*;
import java.lang.*;

public class Ball
{
    /*Properties of the basic ball. These are initialized in the constructor using the values read from the config.xml file*/
	protected int pos_x;			
	protected int pos_y; 				
	protected int radius;
	protected int first_x;			
	protected int first_y;					
	protected int x_speed;			
	protected int y_speed;			
	protected int walls;
	protected int initwalls;
	protected int initradius;
	protected int balltype;
	protected int hitcount;
	Color color;
	AudioClip outSound;
	
    GameWindow gameW;
	Player player;
	
	/*constructor*/
	public Ball (int radius, int initXpos, int initYpos, int speedX, int speedY, int setwalls, int BallType, Color color, AudioClip outSound, Player player,  GameWindow gameW)
	{	
		this.radius = radius;
		this.initradius = radius;

		pos_x = initXpos;
		pos_y = initYpos;

		first_x = initXpos;
		first_y = initYpos;

		x_speed = speedX;
		y_speed = speedY;

		walls = setwalls;
		initwalls = setwalls;
		
		balltype = BallType;
		
		hitcount = 0;

		this.color = color;

		this.outSound = outSound;

		this.player = player;
		this.gameW = gameW;

	}
	
	public void setSpeed()
	{
		Random rand1 = new Random(), rand2 = new Random();
		int x = rand1.nextInt(4)-2;
		int y = rand2.nextInt(4)-2;
		
		if (x == 0 && y == 0)
		{
			x = 1;
		}
		this.x_speed = x;
		this.y_speed = y;
				
	}

	/*update ball's location based on it's speed*/
	public void move ()
	{
		pos_x += x_speed;
		pos_y += y_speed;
		isOut();
	}

	/*when the ball is hit, reset the ball location to its initial starting location*/
	public void ballWasHit ()
	{	
		this.hitcount += 1;
		resetBallPosition();
		this.walls = initwalls;
		if (this.balltype == 2)
		{
			ShrinkBall();
		}
	}

	/*check whether the player hit the ball. If so, update the player score based on the current ball speed. */	
	public boolean userHit (int maus_x, int maus_y)
	{
		player.addClicks(1);
		double x = maus_x - pos_x;
		double y = maus_y - pos_y;

		double distance = Math.sqrt ((x*x) + (y*y));
		
		if (distance-this.radius < (int)(player.scoreConstant)) {
			//player.addScore (player.scoreConstant * Math.abs(x_speed) + player.scoreConstant);
			if (this.balltype == 0)
			{
				player.addScore(30);
			}
			else if (this.balltype == 1)
			{
				player.addScore(20);
			}
			else if (this.balltype == 2)
			{
				x = initradius * 0.3;
				if (radius == initradius)
				{
					player.addScore(10);
				}
				else if (radius > (int)initradius * 0.6)
				{
					player.addScore(20);
				}
				else if (radius > (int)initradius * 0.3)
				{
					player.addScore(40);
				}
				else
				{
					player.addScore(80);
				}
			}
			return true;
		}
		else return false;
	}

    /*reset the ball position to its initial starting location*/
	protected void resetBallPosition()
	{
		pos_x = first_x;
		pos_y = first_y;
		setSpeed();
	}
	
	/*check if the ball is out of the game borders. if so, game is over!*/ 
	protected boolean isOut ()
	{
		if (this.walls > 0)
		{
			if ((pos_x < gameW.x_leftout) || (pos_x > gameW.x_rightout))
			{
				this.x_speed *= -1;
				this.walls -= 1;
			}
			if ((pos_y < gameW.y_upout) || (pos_y > gameW.y_downout))
			{
				this.y_speed *= -1;
				this.walls -= 1;
			}
		}
		else
		{
			if ((pos_x < gameW.x_leftout) || (pos_x > gameW.x_rightout) || (pos_y < gameW.y_upout) || (pos_y > gameW.y_downout)) {	
				resetBallPosition();
			
				outSound.play();
				player.gameIsOver();
				this.walls = initwalls;
		
				return true;
			}	
			else return false;
		}
		return false;
	}

	/*draw ball*/
	public void DrawBall (Graphics g)
	{
		g.setColor (color);
		g.fillOval (pos_x - radius, pos_y - radius, 2 * radius, 2 * radius);
	}
	
	public void ShrinkBall()
	{
		if (this.radius < (0.30 * initradius))
		{
			this.radius = initradius;
		}
		else
		{
			int x = (int)(0.30 * initradius);
			this.radius -= x;
			
		}
	}

}
