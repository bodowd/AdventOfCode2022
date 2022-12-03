import { readFileSync } from "fs";

interface PlayedShape {
  A?: string | undefined;
  B?: string | undefined;
  C?: string | undefined;
  X?: string | undefined;
  Y?: string | undefined;
  Z?: string | undefined;

  [k: string]: string | undefined;
}

interface Points {
  [k: string]: number;
}

const playedMap: PlayedShape = {
  A: "rock",
  B: "paper",
  C: "scissors",
  X: "rock",
  Y: "paper",
  Z: "scissors",
};

const shapePoints: Points = {
  rock: 1,
  paper: 2,
  scissors: 3,
};

const outcomePoints: Points = {
  win: 6,
  draw: 3,
  loss: 0,
};

type Outcome = "win" | "loss" | "draw";

const getOutcome = (
  opponentShapeTranslated: string | undefined,
  yourShapeTranslated: string | undefined
): Outcome => {
  switch (opponentShapeTranslated) {
    case "rock":
      switch (yourShapeTranslated) {
        case "paper":
          return "win";
        case "scissors":
          return "loss";
        case "rock":
          return "draw";
        default:
          console.error("Unknown");
          process.exit(1);
      }
    case "scissors":
      switch (yourShapeTranslated) {
        case "rock":
          return "win";
        case "paper":
          return "loss";
        case "scissors":
          return "draw";
        default:
          console.error("Unknown");
          process.exit(1);
      }
    case "paper":
      switch (yourShapeTranslated) {
        case "scissors":
          return "win";
        case "rock":
          return "loss";
        case "paper":
          return "draw";
        default:
          console.error("Unknown");
          process.exit(1);
      }
    default:
      console.error("Unknown");
      process.exit(1);
  }
};

const getScore = (inputFile: string) => {
  const readFile = readFileSync(inputFile, "utf-8");
  let lines = readFile.split("\n");
  // drop the last element of the array because it's just the empty string
  lines = lines.slice(0, -1);

  let totalScore = 0;
  for (const round of lines) {
    const opponentShape = round[0];
    const yourShape = round[2];
    const opponentShapeTranslated = playedMap[opponentShape];

    const yourShapeTranslated = playedMap[yourShape];

    const outcome = getOutcome(opponentShapeTranslated, yourShapeTranslated);
    if (yourShapeTranslated) {
      const roundScore =
        outcomePoints[outcome] + shapePoints[yourShapeTranslated];
      totalScore += roundScore;
    }
  }
  return totalScore;
};

const main = () => {
  console.log(getScore("example.txt"));
  console.log(getScore("test.txt"));
};

main();
