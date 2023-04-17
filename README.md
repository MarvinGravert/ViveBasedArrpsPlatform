# Input and Tracking System for Augmented Reality-assisted Robot Programming

This repository contains the code associated with the paper: "Input and Tracking System for Augmented Reality-assisted Robot Programming".

An input and tracking system based on the VIVE Lighthouse technology that can act as a basis for _Augmented reality robot programming systems_ (ARRPS) is realized. The system integrates the augmented reality system Hololens. A user programs the path via the VIVE controller while being able to observe the existing waypoints and path through holograms projected by the Hololens. This is demonstrated in the following video.

https://user-images.githubusercontent.com/56734428/180095449-6186b421-a6c3-4670-8d2b-ba70e61058e6.mp4

## Motivation

Robot programming is a complex task and requires highly skilled personal. Making the entire process more approachable is an active research topic. Classically robots are programmed via text or teach panel. Innovation over the last 20 years include _programming by demonstration (PbD) as well as AR an speech. In this paper PbD and AR are combined. To realize this a tracking system is essential. The user input (the demonstration) as well as the AR system has to be referenced to the robot. The Vive offers a low cost off the shelves tracking solution.
The tracker and controller are tracked by the lighthouse using a active marker tracking. Photodiode on the devices are hit by the beams of the ligthhouse which allows to triangulate their relative poses. 

The hololens as the state of the art AR system which also seamlessly integrates with Unity is the choice for the use case.

## System Architecture

The system consists of multiple hardware components: Vive Lighthouse, Vive Tracker, Vive Controller, Hololens and the robot. The frontend is run on the Hololens, the backend on a server. 
![Architecture](https://github.com/MarvinGravert/ViveBasedArrpsPlatform/blob/master/docs/architecture.png)

### Components

The system consists of multiple services which are managed via docker compose.

SteamVR Interface: 

Lighthouse service: 

Registration service: 

Point set registration service

Tracking hub service:

Robot path service: 

## Repo structure
