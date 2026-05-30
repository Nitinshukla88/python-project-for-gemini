pipeline {
    agent any 
    parameters {
        // This is where you define the parameters to include the extra functionality
    }
    environment {
        // here you define the environment variables 
        NEW_VERSION = '1.3.0'
        SERVER_CREDENTIALS = credentials('<here you pass the ID of the credentials in single quote, its important>)
    }
    tools {
        // here you define the tools which helps you in build process like maven, npm etc.
        // but here only three tools are supported - maven, gradle (for backend) and jdk so for more tools, you have to go into tools section of manage jenkins options to add more tools
    }
    stages {
        stage("build") {
            steps {
               /* Here only Linux commands are allowed to write 
               for example echo "hello world " or for node or js environment, you can write sh 'npm run install' or 'npm run build'
              */ 
              echo 'building the application'
              // In groovy syntax, to interpret the string formatting we use double quotes and for normal string we use single quote
              echo "built the version ${NEW_VERSION}" 
              echo 'jenkinsfile for practice'
            }
        }
        stage("test") {
            when {
                expression {
                    // this is where you provide the conditions if they're true then only this stage builds 
                    BRANCH_NAME == 'dev' && <second condition> and so on...
                }
            }
            steps {
                echo 'testing the application'
                echo 'tested the application'
            }
        }
        stage("deploy") {
            steps {
                script {
                    // Inside script, you write the groovy script like :-
                    def val = 2 + 2 > 3 ? 'cool' : 'not cool'
                }
                echo 'deploying the application'
                echo "deployed with credentials ${SERVER_CREDENTIALS}"
            }
        }
    }
    post {
        // this section will run when all the stages will be built completely 
        // it also has section like "always" and some others --> search on the internet
    }
}
