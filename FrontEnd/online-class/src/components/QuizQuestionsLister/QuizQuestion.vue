<template>


<div class="SignInAlignment">
  <form>
        <h3 >#Q : {{questionData.number}} </h3>
        <h4 class="inputStyle" placeholder="Question">{{questionData.text}}</h4>
        <textarea class="inputStyle pa2 " name="message" rows="3" style="width:100%;" :disabled="!editable" placeholder="Your Answer Here"></textarea>
        <textarea class="solutionStyle pa2 " name="message" rows="3" style="width:100%;" disabled v-show="!editable" placeholder="Teacher's Solution" :value="questionData.solution"></textarea>
        <h4>Credit  : {{questionData.credit}}</h4>
  </form>
</div>
</template>

<script>
export default {
  props :{
      questionData :{
        type: Object,
        required:true
      },
      editable:{
        type: Boolean
      }
  },
  data(){
    return{
      questionUserSolution : "",
    }
  },

}
</script>

<style scoped>
.solutionStyle{
    color: cyan !important;
    border-radius: 12px;
background-color: #000000;
background-image: linear-gradient(315deg, #000000 0%, #5e5368 74%);

	  transition-duration: 0.4s;
    border: 2px solid #008CBA;
    width: 100%;
    font-size: 1.5rem;
    padding:8px;
    margin:2px;
}
textarea{
  max-width:100%;
  min-width:100%;
}

h3{
  color:white;
  background-color:white;
  border-radius:12px;
  border: 2px solid #008CBA;
  text-align:left;
  padding:5px;
  width:20% ;
  background-color: #01142F;
	transition-duration: 0.4s;
  cursor:pointer;
}
h4{
    min-height:40px !important;
    cursor:pointer;
}
.SignInAlignment {
    display: flex;
    justify-content : center;
    font-family: "Comic Sans MS", cursive, sans-serif ;
    width: 100%;
    height: 100%;
    opacity: 1 !important;
}

form{
    width:80% !important;
}

.inputStyle {
    color: white !important;
    border-radius: 12px;
    background-color: #01142F;
	  transition-duration: 0.4s;
    border: 2px solid #008CBA;
    width: 100%;
    font-size: 1.5rem;
    padding:8px;
    margin:2px;
}
.row{
  display:flex;
  width:100%;
  height: auto;
}

.buttonStyle:hover {
  background-image: linear-gradient(89deg,#3CBA92,#0BA360);
  color: black ;
}
.otherColumns{
  display: flex;
}
#columnLeft{
  width:20% !important;
  height: auto;
}

#columnRight{
  width:80%  !important;
  height: auto;
}

.buttonStyle{
  border-radius: 12px;
  background-color: powderblue;
  border: none;
  color: black;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  align-content: center;
  font-size: 1rem;
  margin: 4px 2px;
  transition-duration: 0.2s;
  cursor: pointer;
  width: 50%;
  border: 2px solid #008CBA;
}


.buttonStyle:active{
  background-color: royalblue;
  color: red;
  box-shadow: 0 5px #666;
  transform: translateY(2px);
}



.inputStyle:hover{
  border-color:purple;
  background-image: linear-gradient(89deg,#3CBA92,#0BA360);
}
</style>