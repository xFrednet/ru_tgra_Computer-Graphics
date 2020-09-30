#version 330 core
            
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

out vec3 vb_color;

uniform mat4 transformationMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main(){
    vb_color = color;
    gl_Position = transformationMatrix * viewMatrix * projectionMatrix * vec4(position, 1.0);
    gl_Position.w = 1.0;
}