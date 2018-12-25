function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

const scale = (num, in_min, in_max, out_min, out_max) => {
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

var current_question = 0;
var current_score = 0;
var count_correct = 0;
var quiz = [];
var startTime, endTime;

shuffle(two_letter_qs);
shuffle(easy_qs);
shuffle(hard_qs);
shuffle(vocab_qs);

$( document ).ready(function() {
    $("#splash").css("display","block");
    //$("#results").css("display","block");
    //show_results();

    $("#get-info").on('click touch', function () {
    	$("#splash").css("display","none");
    	$("#info").css("display","block");
    });

    $("#get-splash").on('click touch', function () {
    	$("#info").css("display","none");
    	$("#splash").css("display","block");
    });

    $("#start").on('click touch', function () {
    	$("#splash").css("display","none");
    	$("#questions").css("display","block");
    	display_question(current_question);
    });

    $("#choice-a").on('click touch', function () {next_question(0);});
    $("#choice-b").on('click touch', function () {next_question(1);});
    $("#choice-c").on('click touch', function () {next_question(2);});
    $("#choice-d").on('click touch', function () {next_question(3);});

    create_quiz();

});

//built the quiz from the pool of possible questions.
function create_quiz(){
	startTime = new Date();
	quiz = quiz.concat(two_letter_qs.slice(0,10));
	quiz = quiz.concat(easy_qs.slice(0,20));
	quiz = quiz.concat(hard_qs.slice(0,20));
	quiz = quiz.concat(vocab_qs.slice(0,50));
	shuffle(quiz);
}

//change the answers and title to show the next question.
//If there are no more questions, call show_results.
function display_question(q_num){
	//console.log(quiz[q_num]["title"]);

	//update the progress bar
	var progress_bar = Math.round(current_question/quiz.length*100);
	console.log(progress_bar);
	$("#status-progress").css("width",progress_bar+"%")

	if(q_num>=quiz.length){
		//console.log("Done!")
		show_results();
	}else{
		$("#questions-title-span").text(quiz[q_num]["title"]);
		$("#choice-a").text(quiz[q_num][0]);
		$("#choice-b").text(quiz[q_num][1]);
		$("#choice-c").text(quiz[q_num][2]);
		$("#choice-d").text(quiz[q_num][3]);
	}
}

//record the answer, and call display_question() show the next question.
//this also flashes red or green background to indicate a correct answer.
function next_question(user_guess){
	if(quiz[current_question]["answer"]==user_guess){
		//console.log("Right!")
		$("body").animate({
			backgroundColor: "green"
		},200).animate({
			backgroundColor: "white"
		},200);
		current_score+=quiz[current_question]["value"];
		count_correct+=1;
	}else{
		//console.log("Wrong!")
		$("body").animate({
			backgroundColor: "red"
		},200).animate({
			backgroundColor: "white"
		},200);
	}
	$(".choices").animate({color: "#F4F0C0"},200).promise().then(function(){
			//console.log(current_score);
			current_question+=1;
			display_question(current_question);
			$(".choices").animate({color: "black"},200);
		});
}

//When the quiz is complete, calculate the bonus and show the results page.
function show_results(){

		endTime = new Date();
		var timeDiff = endTime - startTime; //in ms
		//to seconds
		timeDiff /= 1000;

		//to minutes
		timeDiff /= 60;

		console.log(timeDiff);

		$("#questions").css("display","none");
    	$("#results").css("display","block");
    	var bonus = Math.floor(scale(current_score, 250, 1000, 300, 10));
    	$("#score").text("+"+bonus);
    	$("#final-score").text(count_correct);
    	$("#question-count").text(quiz.length);
    	$("#final-time").text(Math.round(timeDiff*10)/10);
}