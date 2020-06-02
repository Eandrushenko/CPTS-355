public class Player
{
	private int score;	//player score
	private int clicks;
	private int lives;
	private boolean gameover=false;	
	public int scoreConstant = 15; //This constant value is used in score calculation. You don't need to change this. 
	
	
	public Player()
	{
		score = 0; //initialize the score to 0
		clicks = 0;
		lives = 10;

	}
	/* get player score*/
	public int getScore ()
	{
		return score;
	}
	
	public int getClicks ()
	{
		return clicks;
	}
	
	public int getLives()
	{
		return lives;
	}
	
	/*check if the game is over*/
	public boolean isGameOver ()
	{
		return this.gameover;
	}

	/*update player score*/
	public void addScore (int plus)
	{
		score += plus;
	}
	
	public void addClicks (int plus)
	{
		clicks += plus;
	}

	/*update "game over" status*/
	public void gameIsOver ()
	{
		lives -= 1;
			if (lives < 0)
			{
				gameover = true;
			}
	}
}
	
